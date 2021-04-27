"""
monitor

objects:
- cmd
    - `cmd` objects are strings like `python3 -m openne --clf-ratio 0.2 --dim 128 --early-stopping 20 ...`.
        - They always start with `python3 -m openne`.
        - Arguments follow the format of "--argument-name argument_val [argument_val2 argument_val3...]
            - for detailed format, please refer to OpenNE/readme.md or run `python3 -m openne --help`.
    - `cmd` objects are extremely important in analysis for it provides all settings of an experiment.

input: we deal with 2 kinds of files:
- logs
    - each log stores info of one successful run.
    - looks like (line 1: welcome message; line 2: raw command; line3: parsed training args; line4: result)
        ```
        [OpenNE] This is a welcome message.
        python3 -m openne --clf-ratio 0.8 --dim 64 --early-stopping 20 --epochs 500 --lr 0.001 --patience 3 --dec mlp --enc gin --est jsd --readout sum --sampler node-rand_walk-random --dataset ptc_mr --model ss_graphmodel --task graphclassification
        actual args: {'cpu': False, 'devices': [0], 'task': 'graphclassification', 'model': 'ss_graphmodel', 'dataset': 'ptc_mr', 'local_dataset': False, 'name': 'SelfDefined', 'weighted': False, 'directed': False, 'clf_ratio': 0.8, '_validate': False, '_no_validate': False, 'dim': 64, 'epochs': 500, 'validation_interval': 5, 'debug_output_interval': 5, 'save': False, 'silent': False, 'sparse': False, 'lr': 0.001, 'early_stopping': 20, 'patience': 3, 'enc': 'gin', 'dec': 'mlp', 'sampler': 'node-rand_walk-random', 'est': 'jsd', 'readout': 'sum', 'kstep': 4, 'measurement': 'katz', 'table_size': 100000000.0, 'negative_ratio': 5, 'encoder_layer_list': [128], 'nu1': 1e-08, 'nu2': 0.0001, 'decay': False, 'pretrain': False, 'lamb': 0.4, 'path_length': 80, 'num_paths': 10, 'p': 1.0, 'q': 1.0, 'window': 10, 'workers': 8}
        {'micro': 0.5797101449275363, 'macro': 0.5782929399367756, 'samples': 0.5797101449275363, 'weighted': 0.5800644461752263, 'accuracy': 0.5797101449275363}
        ```
- batch files
    - files of multiple experiments
    - may or may not start with '#!/bin/sh' (must start with this line if you want to run it in `sbatch`
    - multiple cmd lines

"""

from argparse import ArgumentParser
import os
import sys
from multiprocessing import Pool
import subprocess
import re
import json
import datetime
import socket

from typing import Dict, List, Set, Iterable, Sized, Tuple, Union

import tqdm


cur_dir = os.path.abspath(os.path.dirname(__file__))  # directory of this file
root_dir = os.path.normpath(os.path.join(cur_dir, '..', '..'))  # project root, directory of OpenNE
src_dir = os.path.join(root_dir, 'src')  # OpenNE/src
log_dir = os.path.join(src_dir, 'logs')  # OpenNE/src/logs, default path to openne raw logs
processed_dir = os.path.normpath(os.path.join(cur_dir, '..', 'processed'))  #
output_dir = os.path.normpath(os.path.join(processed_dir, 'output'))



if not os.path.exists(output_dir):
    os.makedirs(output_dir)


class CMD:
    """
    Standard class for `cmd` object. This is supposed to use as a comparison & analysis tool for cmd.
    """
    def __init__(self, cmd_str: str):
        """
        Construct a `cmd` object out of a raw string.

        Arguments in the raw string are unordered, so in `__init__()`, we
         - split arguments and store them in `self.args` and
         - sort them in alphabetical order.

        a cmd string of sorted arguments is the standard form of a `cmd` object,
        which is stored in `self.sorted_cmd_str`.

        @param cmd_str: raw string of `cmd` object.
        """
        if not cmd_str.startswith('python'):
            self.args = self.start = self.sorted_cmd_str = None
            return
        self.args = cmd_str.replace('$*', '').strip().replace('  ', ' ').split('--')
        self.start = self.args[0]
        self.args = self.args[1:]
        self.keyval = [arg.split(' ', 1) for arg in self.args]
        self.argsdict = {k: v for k, v in self.keyval}
        self.args.sort()
        self.args = [self.start] + self.args
        self.sorted_cmd_str = '--'.join(self.args)

    def __str__(self):
        """
        provided as standard conversion from `cmd` objects to strings.
        @return: standard (sorted) form
        """
        return self.sorted_cmd_str

    def __repr__(self):
        return str(self)

    def __hash__(self):
        """
        Provided so that you can use `cmd` objects as keys in dicts and sets.

        This is useful since you often need to count experiments and remove repetitive ones.
        @return: hash of standard form
        """
        return hash(str(self))


class RES:
    recognized_criterion = ['micro', 'macro', 'samples', 'weighted']
    @classmethod
    def isresult(cls, res_str):
        try:
            res = eval(res_str)
        except Exception:
            return False
        if not isinstance(res, dict):
            return False
        for criterion in cls.recognized_criterion:
            if criterion not in res:
                return False
        return True

    def __init__(self, res_str):
        try:
            self.res = json.loads(res_str)
        except json.JSONDecodeError:
            self.res = None
        for criterion in self.recognized_criterion:
            if criterion not in self.res:
                self.res[criterion] = None
        self.standard_res = {self.res[criterion]
                             for criterion in self.recognized_criterion}
        self.res_str = ','.join(f'{criterion}: {self.res[criterion]}'
                                for criterion in self.recognized_criterion)
    def __str__(self):
        return self.res_str

    def __repr__(self):
        return str(self)

    def __lt__(self, other: 'RES'):
        for criterion in self.recognized_criterion:
            if self.res[criterion] < other.res[criterion]:
                return True
            if self.res[criterion] > other.res[criterion]:
                return False
        return False

    def __eq__(self, other: 'RES'):
        for criterion in self.recognized_criterion:
            if abs(self.res[criterion] - other.res[criterion]) > 1e-10:
                return False
        return True

    def __le__(self, other: 'RES'):
        for criterion in self.recognized_criterion:
            if self.res[criterion] < other.res[criterion]:
                return True
            if self.res[criterion] > other.res[criterion]:
                return False
        return True



class Cache:
    """
    Cache stores important information about past runs of `monitor.py`.

    The class has only one instance, `cache`, which is used globally.

    In general, `cache` stores important information in a cache file to reduce time-consuming visits to multiple files.
    - For example, OpenNE generates one log file in each run, which contains one cmd string.
      To avoid opening thousands of log files every time we run `monitor.py`, we store
      all pairs of `log files: cmd string` in cache.
    - Another example is experiment progress. We store the number of finished experiments in cache, so we know
      how many new experiments are done since last run of `monitor.py`.

    `cache` is stored as a **json file** and can be parsed as a dict.
    Each item stores certain information, e.g. item `cmd` stores a dict of `log files: cmd string`, as mentioned above.

    `cachefile`: file that stores our cache.
    `keys`: dict of `key: format`.
    - key: item name of cache
    - format: a list. format[0] gives item type. format[1] onwards gives all arguments used to initialize the item in an empty cache.
        - e.g. `'time': [str, 'null']`
            - 'time': there is an item named 'time' in cache
            - str: this 'time' item is stored as string.
            - 'null': in an empty cache (e.g. when we run monitor.py for the first time), we have `time = str('null')`
        - e.g. `'cmd': [dict,]`
            - There is an item named 'cmd', which is a dict.
            - In an empty cache, cmd = dict().
    """
    cachefile = os.path.join(processed_dir, '.monitorcache.json')
    otherfile = os.path.join(processed_dir, '.othermonitorcache.json')
    # `time` stores last write time of cache.
    # `cmd` stores all visited log files and their corresponding cmd strings.
    # `progress` stores all visited batch files and how many experiments in the corresponding files are finished.
    keys = {'time': [str, 'null'], 'cmd': [dict,], 'progress': [dict,]}

    def _merge(self, key, value):
        if key == 'time':
            return  # ignore
        elif key == 'cmd':
            self.cache[key].update(value)
        elif key == 'progress':
            return  # ignore

    def merge(self, othercache):
        for key in self.keys:
            if key in othercache:
                self._merge(key, othercache[key])
                self._write(len(othercache[key]))

    def __init__(self):
        """
        `self.writes`: number of changes to `self.cache`.
        Must only be changed in `self._write()` and `self._force_write()`.
        """

        try:
            with open(Cache.cachefile, 'r') as fd:  # open & read cache file
                self.cache = json.load(fd)
        except Exception:
            self.cache = self.blank()
        # if not os.path.exists(self.cachefile):  # if cache file does not exist
            with open(self.cachefile, 'w') as fd:  # write a blank cache file
                json.dump(self.cache, fd)



        self.writes = 0
        self.update_cache()

        if os.path.exists(self.otherfile):
            try:
                with open(self.otherfile, 'r') as fd:
                    othercache = json.load(fd)
                self.merge(othercache)
            except Exception:
                pass


    def update_cache(self):
        """
        This is used to deal with modifications in cache `keys`.

        If you decide to modify `cache` structure (say, add new key into `Cache.keys`),
        this function helps keeping `cache` up with your modifications.
        """
        for key, typ in self.keys.items():
            if key not in self.cache:
                self.cache[key] = typ[0](*typ[1:])  # standard initialization
                self._write()

    def _force_write(self):
        """
        Force write `self.cache` to cache file. Also change time.
        @return:
        """
        self.cache['time'] = datetime.datetime.now().astimezone(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
        with open(Cache.cachefile, 'w') as fd:
            json.dump(self.cache, fd)
            self.writes = 0
        with open(Cache.otherfile, 'w') as fd:
            json.dump(self.cache, fd)

    def _write(self, num=1):
        """
        Called when self.cache is modified.

        Lazy write. Will only write (_force_write) on every 500 modifications.
        @param num:
        @return:
        """
        self.writes += num
        if self.writes >= 500:
            self._force_write()

    def get_time(self):
        return datetime.datetime.strptime(self.cache['time'], "%Y%m%d_%H%M%S")

    def get_cmd(self) -> dict:
        return self.cache['cmd']

    def write_cmd(self, new_cmd: dict):
        """
        update self.cache['cmd'] with new `log file: cmd` pairs
        @param new_cmd: dict of new `log file: cmd` pairs
        """
        self.cache['cmd'].update(new_cmd)
        self._write(len(new_cmd))

    def get_progress(self):
        return self.cache['progress']

    def write_progress(self, new_progress):
        """
        similar to write_cmd
        @param new_progress:
        @return:
        """
        self.cache['progress'].update(new_progress)
        self._write(len(new_progress))

    def blank(self):
        """
        @return: a blank cache
        """
        return {key: typ[0](*typ[1:]) for key, typ in self.keys.items()}  # standard initialization

    def close(self):
        """
        call before exit. writes all to cache file.
        """
        self._force_write()


cache = Cache()  # the only global Cache instance


def normalcmd(cmd):
    """
    use this small function to normalize cmd.
    @param cmd: (unordered) cmd
    @return:
    """
    return CMD(cmd).sorted_cmd_str

def normalres(res):
    return res


def iscmd(cmd):
    return cmd.startswith('python')


def prefix_of(batch_files, filename: str):
    """
    @param filename: file name to put into batch_files
    @return: file name in batch_files that is prefix of `filename`
    """
    for file in batch_files:
        if filename.startswith(file):
            return file
    return None


def has_prefix(batch_files, filename: str):
    """
    @param filename: file name to put into batch_files
    @return: file name in batch_files that has prefix `filename`
    """
    for file in batch_files:
        if file.startswith(filename):
            return file
    return None


def treeiter(batch_file_tree, name=None):
    if name:
        yield name, batch_file_tree
    for child in batch_file_tree:
        for fruit in treeiter(batch_file_tree[child], child):
            yield fruit


def get_batch_file_tree(path, base_name):
    """
    currently not used
    @param path: -
    @param base_name: -
    @return: -
    """
    files_iter = os.listdir(path)

    batch_file_tree = {}

    for fd in files_iter:
        if fd.endswith('.sh') and prefix_of(base_name, fd):
            fd = fd.rstrip('.sh')
            ptr = batch_file_tree
            while True:
                child = has_prefix(ptr, fd)
                if child is not None:
                    new_node = {child: ptr[child]}
                    ptr.pop(child)
                    ptr[fd] = new_node
                    break
                prefix = prefix_of(ptr, fd)
                if prefix is None:
                    new_node = {}
                    ptr[fd] = new_node
                    break
                ptr = ptr[prefix]

    return batch_file_tree


def search_batch_files(path, base_name, mode='leaf'):
    """
    Two modes: if mode=leaf, keeps only the 'leaf files' in `path` with prefix `base_name` and suffix '.sh'
    e.g. if we have enc.sh, enc_0.sh, enc_1.sh, this will return the latter two files
    if mode==root, keeps only the 'root files'.
    @param path:
    @param base_name: a list of base names
    @param mode: mode selection ['leaf', 'root', 'all']
    @return: a list of files
    """
    files_iter = os.listdir(path)

    batch_files = set()

    def remove(filename: str):
        batch_files.remove(filename)

    def add(filename: str):
        batch_files.add(filename)

    for fd in files_iter:
        if fd.endswith('.sh') and prefix_of(base_name, fd):
            fd = fd.rstrip('.sh')
            if mode == 'leaf':
                prefix = prefix_of(batch_files, fd)
                if prefix is not None:
                    remove(prefix)
                child = has_prefix(batch_files, fd)
                if child is None:
                    add(fd)
            elif mode == 'root':
                child = has_prefix(batch_files, fd)
                while child is not None:
                    remove(child)
                    child = has_prefix(batch_files, fd)
                prefix = prefix_of(batch_files, fd)
                if prefix is None:
                    add(fd)
            else:
                add(fd)

    ret = []
    for fd in batch_files:
        ret.append(os.path.join(path, fd + '.sh'))
    return ret


def parse_output_name(filename):
    kernelname = filename.replace('R-', '').replace('.out', '')
    expname, jobid = kernelname.split('.sh.')
    return expname, jobid


def search_output_files(path, base_name=None, suffix='.out'):
    if base_name is None:
        base_name = ['R-']
    filelist = os.listdir(path)
    output_files = {}
    for filename in filelist:
        #print(">", filename)
        if prefix_of(base_name, filename) and filename.endswith(suffix):
            #print("   good")
            fullname = os.path.abspath(os.path.join(path, filename))
            expname, jobid = parse_output_name(filename)
            ti_c = os.path.getctime(fullname)
            if expname in output_files:
                oldfilename, old_tic = output_files[expname]
                if old_tic < ti_c:
                    output_files[expname] = (fullname, ti_c)
            else:
                output_files[expname] = (fullname, ti_c)
    return output_files


def get_outputs(output_filenames):

    outputs = {}
    for filename in output_filenames:
        #print(filename, ":")
        outputs[filename] = {}
        with open(filename, 'r') as fd:
            READY, GOT_CMD = 0, 1
            cur_st = READY
            cur_cmd = None
            cur_res = None
            for line in fd:
                if iscmd(line):
                #    print("  got cmd")
                    if cur_st == READY:
                        cur_cmd = normalcmd(line)
                        cur_st = GOT_CMD
                    else:
                    #    print("unknown error")
                        outputs[filename][cur_cmd] = "unknown error"
                        cur_cmd = normalcmd(line)
                        # cur_st = GOT_CMD
                elif RES.isresult(line):
                #    print("  is result")
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = int(eval(line)['micro'] * 1000) / 1000
                        cur_st = READY
                elif line.find('NaN') >= 0:
                #    print("  NaN")
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = 'NaN'
                        cur_st = READY
                elif line.find('Killed') >= 0:
                #    print("  Killed")
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = 'killed'
                        cur_st = READY
                elif line.find('CUDA') >= 0:
                #    print("  CUDA")
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = 'cuda error'
                        cur_st = READY
                elif line.find('Error:') >= 0:
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = line
                        cur_st = READY
            # if cur_cmd == READY:
            #     outputs[filename][cur_cmd] = "Unknown error"
        # print(len(outputs[filename]))
    return outputs


def outputs_to_csv(outputs):
    # merge all outputs in different files
    all_outputs = []
    for i in outputs:
        all_outputs.extend(outputs[i].items())
    recognized_args = ['dataset', 'enc', 'dec', 'sampler', 'readout', 'est', 'dim', 'hiddens']
    csv_head = ','.join(recognized_args) + ',result'
    csv_lines = []
    for cmd, res in all_outputs:
        argsdict = CMD(cmd).argsdict
        args = []
        for arg in recognized_args:
            if arg not in argsdict:
                val = '-'
            else:
                val = argsdict[arg]
            args.append(val)
        csv_lines.append(','.join(args) + ',' + str(res))
    csv_text = '\n'.join([csv_head] + csv_lines)
    csv_name = 'failure_analysis.csv'
    fullname = os.path.join(processed_dir, csv_name)
    with open(fullname, 'w') as fd:
        fd.write(csv_text)
    print(f"Wrote runtime failure analysis to {fullname}.")



def get_slurm_outputs(batch_path, base_name):
    output_file_dict = search_output_files(batch_path, base_name)
    output_filenames = {fullname for (fullname, _) in output_file_dict.values()}
    outputs = get_outputs(output_filenames)
    return outputs, output_file_dict

def warn(e):
    # print(e)
    pass


def log(*args, **kwargs):
    print(*args, **kwargs)


def get_command(f) -> Union[None, str]:
    """
    get cmd from file
    @param f: **file handler**
    @return: normal form of cmd if found; None if not found
    """
    for pline in f:
        if pline.startswith('python'):  # recognized as command
            return normalcmd(pline)
    return None


def get_command_and_result(f) -> Tuple:
    cmd = res = None
    for pline in f:
        if pline.startswith('python'):
            cmd = normalcmd(pline)
        elif pline.startswith('{'):
            res = normalres(pline)

    return cmd, res


def get_logs_from_file_list(arg):
    """
    Open multiple log files and extract their cmd info.

    This function is run in multiple processes to boost speed.

    @param arg: [procnum, path, files_iter, cache_command,]
        procnum: `int`, indicates process id
        path: path to find log files
        files_iter: `Iterable`, a bunch of filenames (just filenames without path)
        cache_command: `dict`, 'command' items in cache

    @return: [procnum, logs, new_logs]
        logs: str, all cmd strings found (normal form)
        new_logs: dict, new `log file: cmd` items (used to update cache)
    """
    procnum, path, files_iter, cache_command = arg[:4]
    logs = []
    new_logs = {}
    try:
        for ni, fd in enumerate(files_iter):
            if fd in cache_command:
                command = cache_command[fd]
            else:
                command = None
                try:
                    with open(os.path.join(path, fd), 'r') as f:
                        command = get_command(f)
                        # command, res = get_command_and_result(f)
                        new_logs[fd] = command
                except Exception as e:
                    warn(e)
                    new_logs[fd] = None
            if command is not None:
                logs.append(command)
    except Exception as e:
        print(e)
    return procnum, logs, new_logs


def search_logs(path):
    """
    Search for all log files in `path` and extract their cmd info.
    @param path: path to log files.
    @return: a set of all cmd strings.
    """
    files = os.listdir(path)  # all files (not necessarily log files)
    files.sort()  # so they are sorted by time; in case you need to overwrite replicated experiments

    # multiprocessing

    # split into n_split processes
    n_split = 100

    # split the files into `n_split` parts
    n_files = len(files)
    sub_size = (n_files + n_split - 1) // n_split

    # get cache to boost speed
    cache_cmd = cache.get_cmd()

    # prepare args to feed to `get_logs_from_file_list`
    multiprocess_args = [(i, path, files[i * sub_size: (i + 1) * sub_size], cache_cmd) for i in range(n_split)]

    # multiprocessing and data collect
    log("Searching for logs...")
    ret_list = []
    with Pool(n_split) as p:
        for whatever_x in tqdm.tqdm(p.imap_unordered(get_logs_from_file_list, multiprocess_args), total=n_split):
            ret_list.append(whatever_x)  # whatever_x: retval from get_logs_from_file_list

    # this is why we pass procnum into `get_logs_from_file_list`:
    # Pool.imap_unordered returns a list of results in random order
    # so we must restore order through a sort
    # Recall that `get_logs_from...` returns [procnum, logs, new_logs]
    ret_list.sort(key=lambda x: x[0])
    all_commands = []
    all_new_cmds = {}
    for k in range(n_split):
        all_commands.extend(ret_list[k][1])
        all_new_cmds.update(ret_list[k][2])
    cache.write_cmd(all_new_cmds)

    # get logs from cache in case they are from .othermonitorcache.json
    all_commands = cache.get_cmd().values()

    log(f'Found {len(set(all_commands))} logs.')
    return set(all_commands)


def get_files(filenames) -> Dict[str, List[str]]:
    """
    A basic operation. Mainly used in `get_cmd()` below.

    Read a list of files. For each file, read all
    lines as a list, and put item `file: lines` in the returning dict
    @param filenames: a list of files (full path)
    @return: dict of `file: lines`
    """
    ret = {}
    for file in filenames:
        ret[file] = list(open(file, 'r'))
    return ret


def get_cmd(filenames) -> Dict[str, List[str]]:
    """
    Get all cmd lines in a list of batch files.

    call `get_files` first, and normalize each cmd line.
    @param filenames: a list of files (full path)
    @return:
    """
    r1 = get_files(filenames)
    ret = {}
    for file, val in r1.items():
        ret[os.path.basename(file)] = [normalcmd(x) for x in val if iscmd(x)]
    return ret


def check_progress(batch_cmd: Dict[str, List], logs: Set) \
        -> (Dict[str, Set], Dict[str, Tuple[int]]):
    finished_cmd = {}
    finished_ratio = {}
    for batch_file in batch_cmd:
        finished_cmd[batch_file] = logs.intersection(batch_cmd[batch_file])
        finished_ratio[batch_file] = (len(finished_cmd[batch_file]), len(batch_cmd[batch_file]))

    return finished_cmd, finished_ratio


def get_unfinished(batch_cmd: Dict[str, Iterable], finished_cmd: Dict[str, Iterable]) \
        -> Dict[str, set]:
    unfinished_cmd = {}
    for batch_file in batch_cmd:
        unfinished_cmd[batch_file] = set(batch_cmd[batch_file]).difference(finished_cmd[batch_file])

    return unfinished_cmd


def read_files(batch_path, base_name, log_path):
    batch_files = search_batch_files(batch_path, base_name)
    batch_cmd = get_cmd(batch_files)
    logs = search_logs(log_path)
    return batch_cmd, logs


def show_batch_info(batch_files, batch_info, running_jobs=None, title=None, title_description=None):
    if running_jobs is None:
        running_jobs = {}
    if title is None:
        title = "Batch info"
    if title_description is None:
        title_description = ''

    highlight_color = "\033[33m\033[1m\033[4m"
    default_color = "\033[0m"

    print(f"{title} (running jobs are {highlight_color}highlighted{default_color}): {title_description}")

    batch_files_sorted = list(batch_files)
    batch_files_sorted.sort(key=lambda x: '0' + x if x in running_jobs else '1' + x)
    for batch_file in batch_files_sorted:
        if batch_file in running_jobs:
            begin_color = highlight_color
            end_color = default_color
            description = f"(ID {running_jobs[batch_file].jobid})"
        else:
            begin_color = ""
            end_color = ""
            description = ""
        print(f"{begin_color}{batch_file}{end_color}{description}: {batch_info[batch_file]}")
    print()


def show_exp_progress(batch_path, base_name, log_path, running_jobs=None):
    """
    display
    @param batch_path:
    @param base_name:
    @param log_path:
    @param running_jobs:
    @return:
    """
    batch_cmd, logs = read_files(batch_path, base_name, log_path)
    finished_cmd, finished_ratio = check_progress(batch_cmd, logs)

    progress = cache.get_progress()
    new_progress = {}
    progress_val = {}
    for file in batch_cmd:
        if file not in progress or progress[file] != finished_ratio[file][0]:
            new_progress[file] = finished_ratio[file][0]
            value = finished_ratio[file][0]
            if file in progress:
                value -= progress[file]
            progress_val[file] = f'+{value}'
        else:
            progress_val[file] = '+0'

    cache.write_progress(new_progress)

    # display

    progress_color = "\033[32m\033[1m"
    static_color = "\033[34m\033[1m"
    default_color = "\033[0m"

    title = 'Experiment progress'
    batch_files = list(batch_cmd.keys())
    batch_info = {batch_file: f'{finished_ratio[batch_file][0]}'
                              f'/{finished_ratio[batch_file][1]}'
                              f'    {progress_color if batch_file in new_progress else static_color}'
                              f'{progress_val[batch_file]}'
                              f'{default_color}'
                  for batch_file in batch_files}
    title_description = \
        f"{sum(finished_ratio[batch_file][0] for batch_file in batch_files)}" \
        f"/{sum(finished_ratio[batch_file][1] for batch_file in batch_files)}"
    show_batch_info(batch_files, batch_info, running_jobs, title, title_description)


def write_exps(explist):
    """
    write file
    @param explist:
    @return:
    """
    ret = []
    for filename in explist:
        lastname = os.path.basename(os.path.normpath(filename))
        w_name = os.path.join(output_dir, lastname)
        with open(w_name, 'w') as fd:
            fd.write('#!/bin/sh\n')
            fd.write('\n'.join(explist[filename]))
        ret.append(w_name)
    return ret


def refresh_exps(batch_path, base_name, log_path, running_jobs=None, display=True, failure_args=None):
    batch_cmd, logs = read_files(batch_path, base_name, log_path)
    finished_cmd, finished_ratio = check_progress(batch_cmd, logs)
    unfinished = get_unfinished(batch_cmd, finished_cmd)

    # combine failure args
    new_exps = unfinished
    if failure_args is not None:
        r_base_name = ['R-' + name for name in base_name]
        outputs, output_file_dict = get_slurm_outputs(batch_path, r_base_name)
        for batch_file in batch_cmd:
            exp_name = os.path.basename(batch_file).replace('.sh', '')
            # print(exp_name)
            if exp_name in output_file_dict:
                output_file_name, _ = output_file_dict[exp_name]
                _, jobid = parse_output_name(output_file_name)

                output_info = outputs[output_file_name]
                for cmd in output_info:
                    if failure_args.err == False:
                        if isinstance(output_info[cmd], str) and cmd in new_exps[batch_file]:
                            new_exps[batch_file].remove(cmd)
                    else:
                        if failure_args.killed == False:
                            if output_info[cmd] == 'killed' and cmd in new_exps[batch_file]:
                                new_exps[batch_file].remove(cmd)
                        if failure_args.nan == False:
                            if output_info[cmd] == 'NaN' and cmd in new_exps[batch_file]:
                                new_exps[batch_file].remove(cmd)
    ret = write_exps(new_exps)

    # display
    if display:
        title = f"Write to {output_dir}"
        batch_files = list(batch_cmd.keys())
        batch_info = {filename: f"wrote {len(new_exps[filename])} "
                                f"remaining experiment"
                                f"{'s' if len(new_exps[filename]) > 1 else ''}"
                                f" out of {len(batch_cmd[filename])} total"
                      for filename in new_exps}
        show_batch_info(batch_files, batch_info, running_jobs, title)

    return ret


def parse_common_args(args):
    batch_path = args.srcdir
    log_path = args.logdir
    base_name = args.base
    base_names = [base_name + range_name for range_name in args.range]
    return batch_path, base_names, log_path


class JobBlock:
    def __init__(self, jobid, partition, name, *args, **kwargs):
        self.jobid = jobid
        self.partition = partition
        self.name = name

    def __str__(self):
        return f"JOB {self.jobid}: {self.partition}, {self.name}"

    def __repr__(self):
        return str(self)


class JobBlockManager:
    def __init__(self, it: Iterable[JobBlock]):
        self.jobs = {job.name: job for job in it}

    def __contains__(self, item):
        return item in self.jobs

    def __iter__(self):
        return self.jobs

    def __getitem__(self, item):
        return self.jobs[item]


def get_running_jobs():
    output = subprocess.check_output(
        ['squeue', '--format', '%.8i %.9P %100j', '--user', os.getenv('USER')],
    ).decode('utf-8')
    jobs = JobBlockManager([JobBlock(*line.split(None)) for line in output.strip().split('\n')][1:])
    return jobs


def get_partition():
    output = subprocess.check_output(
        ['sinfo']
    ).decode('utf-8')
    regex = re.compile('[^\\w]')
    partitions = [regex.sub('', line.split(None, 1)[0]) for line in output.strip().split('\n')][1:]
    return partitions


def parse_show(args):
    batch_path, base_name, log_path = parse_common_args(args)
    jobs = get_running_jobs()
    show_exp_progress(batch_path, base_name, log_path, jobs)


def parse_gen(args):
    batch_path, base_name, log_path = parse_common_args(args)
    jobs = get_running_jobs()
    refresh_exps(batch_path, base_name, log_path, jobs)


def run_job_sbatch(name, partition, failure_args=None):
    modify_batch = False
    with open(name, 'r') as fd:
        lines = list(fd)
        if len(lines) == 0 or not lines[0].startswith('#!'):
            modify_batch = True

    if modify_batch:
        with open(name, 'w') as fd:
            fd.write("#!/bin/sh\n")
            fd.write('\n'.join(lines))
    tmpdir = os.path.abspath(os.curdir)
    os.chdir(src_dir)
    print(f"run {name} at {os.path.abspath(os.curdir)} with partition {partition}")
    subprocess.run(['sbatch', '-G', '1', '-p', partition, '--output=R-%x.%j.out', name])
    os.chdir(tmpdir)
    # subprocess.run(['sbatch', '-G', '1', '-p', partition, name])


def stop_job_sbatch(name, jobid):
    print(f"stop {name} (jobid: {jobid})")
    subprocess.run(['scancel', jobid])


def run_batch_files(batch_file_names, partitions, failure_args=None):
    for name in batch_file_names:
        run_job_sbatch(name, partitions[0], failure_args)


def stop_batch_files(batch_file_names, jobs):
    for name in batch_file_names:
        if os.path.basename(name) in jobs:
            stop_job_sbatch(name, jobs[os.path.basename(name)].jobid)

def parse_failure_args(args):
    class Tmp:
        def __init__(self):
            self.nan = True
            self.killed = True
            self.err = True

    ret = Tmp()
    attrs = ['nan', 'killed', 'err']
    for attr in attrs:
        setattr(ret, attr, getattr(args, attr, True))
    return ret

def parse_run(args):
    batch_path, base_name, log_path = parse_common_args(args)
    failure_args = parse_failure_args(args)
    jobs = get_running_jobs()
    partitions = get_partition()
    if len(partitions) == 0:
        print("No partitions available!")
        exit(1)

    #  update experiment
    batch_file_names = refresh_exps(batch_path, base_name, log_path, jobs, failure_args)

    #  do not update
    # batch_file_names = search_batch_files(batch_path, base_name)
    # for name in batch_file_names:
    #     if os.path.basename(name) not in jobs:
    #         run_job_sbatch(name, partitions[0])
    all_batch_file_names = search_batch_files(batch_path, base_name, 'all')
    stop_batch_files(all_batch_file_names, jobs)
    run_batch_files(batch_file_names, partitions)


def parse_stop(args):
    batch_path, base_name, log_path = parse_common_args(args)
    jobs = get_running_jobs()

    batch_file_names = search_batch_files(batch_path, base_name, 'all')
    stop_batch_files(batch_file_names, jobs)

def parse_check(args):
    batch_path, base_name, log_path = parse_common_args(args)
    r_base_name = ['R-' + name for name in base_name]
    jobs = get_running_jobs()
    outputs, output_file_dict = get_slurm_outputs(batch_path, r_base_name)
    # display outputs
    batch_cmd, logs = read_files(batch_path, base_name, log_path)
    finished_cmd, finished_ratio = check_progress(batch_cmd, logs)

    # display

    title = 'Runtime Analysis'
    batch_files = list(batch_cmd.keys())
    batch_info = {}
    for batch_file in batch_files:

        finished_str = f'{finished_ratio[batch_file][0]}'\
                       f'/{finished_ratio[batch_file][1]}'\
                       f' finished'
        exp_name = os.path.basename(batch_file).replace('.sh', '')
        # print(exp_name)
        if exp_name in output_file_dict:
            output_file_name, _ = output_file_dict[exp_name]
            _, jobid = parse_output_name(output_file_name)

            output_info = outputs[output_file_name]
            #if len(output_info) < 2:
            #    print(exp_name, output_info)
            error_dict = {}
            for _, res in output_info.items():
                if isinstance(res, str):  # an error
                    if res.find(':'):
                        res = res.split(':')[0]
                    error_dict[res] = error_dict.get(res, 0) + 1
                else:
                    error_dict['successful'] = error_dict.get('successful', 0) + 1
            killed_str = ', ' + ', '.join(f'{cnt} {res}' for res, cnt in error_dict.items())

            batch_info[batch_file] = finished_str + f' (ID {jobid})' + killed_str
        else:
            batch_info[batch_file] = finished_str
    show_batch_info(batch_files, batch_info, jobs, title)
    outputs_to_csv(outputs)
    # show_batch_info(batch_files)

PORT = 64531

def get_ipv4():  # https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

    # output = subprocess.check_output(
    #     ['sinfo']
    # ).decode('utf-8')
    # regex = re.compile('[^\\w]')
    # partitions = [regex.sub('', line.split(None, 1)[0]) for line in output.strip().split('\n')][1:]
    # return partitions

HOST = get_ipv4()
blocksize = 1024
clearline = '\r' + ' ' * 30 + '\r'
endingbytes = b'```eof```'

def receive_data(socket):
    data = b''
    exitflag = False
    while not exitflag:
        block = socket.recv(blocksize)
        data += block
        if data.endswith(endingbytes):
            exitflag = True
            data = data.replace(endingbytes, b'')

        print(clearline, end='')
        print(f"({len(data)} bytes received.)", end='', flush=True)
    print(f"(All received.)", flush=True)
    print(data.decode('utf-8')[-200:])
    return data

def send_data(socket, data):
    print(f"({len(data)} to send...)")
    print(data.decode('utf-8')[-200:])
    for i in range(0, len(data), blocksize):
        socket.sendall(data[i:i + blocksize])
        print(clearline, end='')
        print(f"({i + len(data[i:i + blocksize])} bytes sent.)", end='', flush=True)
    socket.sendall(endingbytes)
    print(f"(All sent.)", flush=True)

def parse_sync(args):

    print(f"local IPv4: {HOST}")
    if args.server == 'self':
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print("Waiting for connection. "
                  "Use the following command on another server to sync data:")
            print()
            print(f"python monitor.py sync --server {HOST}")
            print()
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr}.')
                data = receive_data(conn)
                cache_block = json.loads(data.decode('utf-8'))
                cache.merge(cache_block)
                cachedata = json.dumps(cache.cache).encode('utf-8')
                send_data(conn, cachedata)
                print("Sync completed.")
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting...")
            s.connect((args.server, PORT))
            print(f"Connected to {args.server}.")
            cachedata = json.dumps(cache.cache).encode('utf-8')
            send_data(s, cachedata)
            data = receive_data(s)
            cache_block = json.loads(data.decode('utf-8'))
            cache.merge(cache_block)
            print("Sync completed.")





parser = ArgumentParser()
subparsers = parser.add_subparsers()
parser_show = subparsers.add_parser('show', help='Show experiment progress.')
parser_gen = subparsers.add_parser('gen', help='Generate new experiment settings.')
parser_run = subparsers.add_parser('run', help='Run experiments.')
parser_stop = subparsers.add_parser('stop', help='Stop experiments.')
parser_sync = subparsers.add_parser('sync', help='Sync between multiple servers.')
parser_check = subparsers.add_parser('check', help='Check experiment status.')
for parserx in [parser_show, parser_gen, parser_run, parser_stop, parser_check]:
    parserx.add_argument('--base', default='autogen_sample_script_', help='Provide base name for autogen script.')
    parserx.add_argument('--range', nargs='*', default=[''],
                         help='Select process range for autogen script.')
    parserx.add_argument('--srcdir', default=src_dir, help='Path to autogen script.')
    parserx.add_argument('--logdir', default=log_dir, help='Path to logs.')
parser_sync.add_argument('--server', default='self', help='Address of server. By default this machine will be server.')
parser_run.add_argument('--no-nan', action='store_false', dest='nan', help='Do not run experiments that have produced NaN.')
parser_run.add_argument('--no-killed', action='store_false', dest='killed', help='Do not run experiments that are killed by slurm.')
parser_run.add_argument('--no-fail', action='store_false', dest='fail', help='Do not run experiments that have failed.')

parser_show.set_defaults(func=parse_show)
parser_gen.set_defaults(func=parse_gen)
parser_run.set_defaults(func=parse_run)
parser_stop.set_defaults(func=parse_stop)
parser_sync.set_defaults(func=parse_sync)
parser_check.set_defaults(func=parse_check)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
    cache.close()
