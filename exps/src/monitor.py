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
        python3 -m openne --clf-ratio 0.8 --dim 64 --early-stopping 20 --epochs 500 --lr 0.001 \
        --patience 3 --dec mlp --enc gin --est jsd --readout sum --sampler node-rand_walk-random \
        --dataset ptc_mr --model ss_graphmodel --task graphclassification
        actual args: {'cpu': False, 'devices': [0], 'task': 'graphclassification', ...}
        {'micro': 0.5797101449275363, 'macro': 0.5782929399367756, 'samples': ..., 'weighted': ..., 'accuracy': ...}
        ```
- batch files
    - files of multiple experiments
    - may or may not start with '#!/bin/sh' (must start with this line if you want to run it in `sbatch`
    - multiple cmd lines

"""
import getpass
import itertools
import random
from argparse import ArgumentParser
import os
import sys
from multiprocessing import Pool
import subprocess
import re
import json
import datetime
import socket
from pathlib import Path
from time import sleep, time

try:
    import daemon
except ModuleNotFoundError:
    subprocess.run(['pip', 'install', 'python-daemon'])
    import daemon

from typing import Dict, List, Set, Iterable, Sized, Tuple, Union, Any, Optional

import tqdm

cur_dir = os.path.abspath(os.path.dirname(__file__))  # directory of this file
root_dir = os.path.normpath(os.path.join(cur_dir, '..', '..'))  # project root, directory of OpenNE
src_dir = os.path.join(root_dir, 'src')  # OpenNE/src
log_dir = os.path.join(src_dir, 'logs')  # OpenNE/src/logs, default path to openne raw logs
processed_dir = os.path.normpath(os.path.join(cur_dir, '..', 'processed'))  #
output_dir = os.path.normpath(os.path.join(processed_dir, 'output'))

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


class CMD(str):
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
        self.argsdict = {}
        for itm in self.keyval:
            if len(itm) == 1:
                self.argsdict[itm[0]] = None
            else:
                self.argsdict[itm[0]] = itm[1].strip()
        self.args.sort()
        self.args = [self.start] + self.args
        self.sorted_cmd_str = '--'.join(self.args)

    def sync(self):
        self.keyval = [(k, v) for k, v in self.argsdict.items()]
        self.args = [f'{k} {v}' for k, v in self.keyval]
        self.args.sort()
        self.args = [self.start] + self.args
        self.sorted_cmd_str = '--'.join(self.args)

    def change_key(self, key, val):
        self.argsdict[key] = val
        self.sync()

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


def normalcmd(cmd):
    """
    use this small function to normalize cmd.
    @param cmd: (unordered) cmd
    @return:
    """
    return CMD(cmd).sorted_cmd_str


class RES(dict):
    recognized_criterion = ['micro', 'macro', 'samples', 'weighted']

    @classmethod
    def fromdict(cls, d: dict):
        return RES(json.dumps(d))

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

    def __init__(self, res_str=None):
        super(RES, self).__init__()
        if res_str is None:
            self.res = self.empty_res()
        else:
            try:
                self.res = json.loads(res_str.replace("'", '"'))
            except json.JSONDecodeError:
                self.res = self.empty_res()
                print("decode err", res_str)
        for criterion in self.recognized_criterion:
            if criterion not in self.res:
                self.res[criterion] = None
        self.standard_res = {criterion: self.res[criterion]
                             for criterion in self.recognized_criterion}
        self.update(self.standard_res)
        self.res_str = json.dumps(self.standard_res)

    def simple(self):
        if self.res['micro'] is None:
            return str('-')
        return str(int(self.res['micro'] * 1000) / 1000)

    def isvalid(self):
        for criterion in self.recognized_criterion:
            if self.res[criterion] is None:
                return False
        return True

    @classmethod
    def empty_res(cls):
        return {a: None for a in cls.recognized_criterion}

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


class STATUS(str):
    _FINISHED = 'finished'
    _UNFINISHED = 'unfinished'
    _KILLED = 'killed'
    _CUDAERR = 'cudaerr'
    _NAN = 'nan'
    _OTHERS = 'others'
    _UNKNOWN = 'unknown'
    recognized_status = [_FINISHED, _UNFINISHED, _KILLED, _CUDAERR, _NAN, _OTHERS, _UNKNOWN]

    def __init__(self, s: Optional[str] = None):
        if s is None:
            s = self._UNKNOWN
        s = s.strip()
        if s in self.recognized_status:
            self.status = s
            self.description = ''
        else:
            self.status = self._OTHERS
            self.description = self.status
        super().__init__()

    def is_cudaerr(self):
        return self.status == self._CUDAERR

    def is_finished(self):
        return self.status == self._FINISHED

    def is_unfinished(self):
        return self.status == self._UNFINISHED

    def is_nan(self):
        return self.status == self._NAN

    def is_others(self):
        return self.status == self._OTHERS

    def is_killed(self):
        return self.status == self._KILLED

    def is_failed(self):
        return self.status == self._CUDAERR or self._NAN or self._KILLED or self._OTHERS

    @classmethod
    def parse_status_from_line(cls, line: str):
        if line.find('NaN') >= 0:
            return STATUS(cls._NAN)
        if line.find('Killed') >= 0:
            return STATUS(cls._KILLED)
        if line.find('CUDA') >= 0:
            return STATUS(cls._CUDAERR)
        if line.find('Error:') >= 0:
            return STATUS(line)
        return STATUS(cls._UNKNOWN)

    def __str__(self):
        return self.status

    def __eq__(self, other: str):
        return self.status == str(other)


STATUS.FINISHED = STATUS(STATUS._FINISHED)
STATUS.UNFINISHED = STATUS(STATUS._UNFINISHED)
STATUS.KILLED = STATUS(STATUS._KILLED)
STATUS.CUDAERR = STATUS(STATUS._CUDAERR)
STATUS.NAN = STATUS(STATUS._NAN)
STATUS.OTHERS = STATUS(STATUS._OTHERS)
STATUS.UNKNOWN = STATUS(STATUS._UNKNOWN)


class EXP(dict):
    def __init__(self, cmd: CMD, status: STATUS, res: Optional[RES] = None, timestamp: Any = None):
        super().__init__()
        self.update({"cmd": cmd, "status": status, "res": res, "timestamp": timestamp})

    def todict(self):
        try:
            return {'cmd': str(self['cmd']), 'status': str(self['status']), 'res': dict(self['res']),
                    'timestamp': self['timestamp']}
        except Exception:
            print(self['cmd'], self['status'], self['res'], self['timestamp'])
            exit(0)

    @classmethod
    def fromcmdstr(cls, cmdstr: str):
        cmd = CMD(cmdstr)
        # print("EXP says: ", cmd)
        if 'fakecmd' in cmd.argsdict:
            cmd = CMD(cmdstr.replace('--fakecmd', ''))
            status = STATUS.UNFINISHED
            # print("fake command, ", status)
        else:
            status = STATUS.UNKNOWN
        return EXP(cmd, status)

    @classmethod
    def fromlogfilehandler(cls, f):
        res = None
        exp = None
        for pline in f:
            if iscmd(pline):
                exp = EXP.fromcmdstr(pline)

            elif pline.startswith('{'):
                # print("get res")
                res = RES(pline)
                # print("RES:", json.dumps(str(res)))
        if exp is not None and res is not None:
            exp['res'] = res
            if res.isvalid():
                exp['status'] = STATUS.FINISHED
        # print("EXP:", dict(exp))
        return exp

    @classmethod
    def fromlogfile(cls, logfilename: str):
        with open(logfilename, 'r') as f:
            return cls.fromlogfilehandler(f)

    @classmethod
    def fromdict(cls, d: dict):
        # print("from dict:", CMD(d['cmd']))
        return EXP(CMD(d['cmd']), STATUS(d['status']), RES.fromdict(d['res']), d['timestamp'])

    @classmethod
    def fakelogfile(cls, cmdstr: str):
        filename = os.path.join(log_dir, "_".join((
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + str(time() * 10000000)[-9:],
            "fake_log", ".txt")
        ))
        with open(filename, 'w') as f:
            f.write('[Fake log] This is a fake log.\n' + cmdstr + ' --fakecmd' + '\n?\n' + str(RES()))

    @classmethod
    def merge_exp_table(cls, old_dict, new_dict):
        for k, v in new_dict.items():
            if k not in old_dict:
                old_dict[k] = v
            elif old_dict[k]['timestamp'] is None:
                continue
            elif v['timestamp'] is None:
                old_dict[k] = v
            elif old_dict[k]['timestamp'] < v['timestamp']:
                old_dict[k] = v


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
    keys = {'version': [int, 4], 'time': [str, 'null'], 'cmd': [dict, ], 'progress': [dict, ], 'status_table': [dict, ]}

    def _merge(self, key, value):
        if key == 'time':
            return  # ignore
        elif key == 'cmd':
            for k, v in value.items():
                if k not in self.cache[key]:
                    self.cache[key][k] = v
            # self.cache[key].update(value)
        elif key == 'progress':
            return  # ignore
        elif key == 'status_table':
            EXP.merge_exp_table(self.cache[key], value)

    def merge(self, othercache):
        if othercache.get('version', -1) < self.cache['version']:
            return  # no merge
        for key in self.keys:
            if key in othercache:
                self._merge(key, othercache[key])
                self._write()

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
        if self.cache.get('version', -1) < self.keys['version'][1]:
            self.cache = self.blank()
            with open(self.cachefile, 'w') as fd:  # write a blank cache file
                json.dump(self.cache, fd)
            return
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
        for key in new_cmd:
            new_val = new_cmd[key].todict()
            self.cache['cmd'][key] = new_val
        # self.cache['cmd'].update(new_cmd)
        self._write(len(new_cmd))
        # print("WWWWWWW")

    def get_status_table(self) -> dict:
        return self.cache['status_table']

    def write_status_table(self, new_status_table: dict):
        """
        update self.cache['cmd'] with new `log file: cmd` pairs
        @param new_cmd: dict of new `log file: cmd` pairs
        """
        for key in new_status_table:
            new_val = new_status_table[key].todict()
            self.cache['status_table'][key] = new_val
        # self.cache['cmd'].update(new_cmd)
        self._write(len(new_status_table))

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


def normalres(res):
    return RES(res)


def iscmd(cmd):
    return cmd.startswith('python')


def prefix_of(batch_files, filename: str, self_contain=True, longest=False):
    """
    @param filename: file name to put into batch_files
    @return: file name in batch_files that is prefix of `filename`
    """
    longestfile = None
    for file in batch_files:
        if filename.startswith(file) and (self_contain or filename != file):
            if not longest:
                return file
            else:
                if longestfile is None or len(longestfile) < len(file):
                    longestfile = file
    return longestfile


def has_prefix(batch_files, filename: str, self_contain=True):
    """
    @param filename: file name to put into batch_files
    @return: file name in batch_files that has prefix `filename`
    """
    for file in batch_files:
        if file.startswith(filename) and (self_contain or filename != file):
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

            fd = fd.replace('.sh', '')
            # print("?found", fd)
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


def search_output_files(path, base_name=None, suffix='.out', all_files=True):
    assert all_files is True, '`all_files` must be True!'
    if base_name is None:
        base_name = ['R-']
    filelist = os.listdir(path)
    output_files = {}
    for filename in filelist:
        # print(">", filename)
        if prefix_of(base_name, filename) and filename.endswith(suffix):
            # print("   good")
            fullname = os.path.abspath(os.path.join(path, filename))
            expname, jobid = parse_output_name(filename)
            ti_c = os.path.getctime(fullname)
            if expname in output_files:
                if all_files:
                    output_files[expname].append((fullname, ti_c))
                else:  # we keep the original implementation but make it deprecated
                    oldfilename, old_tic = output_files[expname]
                    if old_tic < ti_c:
                        output_files[expname] = [(fullname, ti_c)]
            else:
                output_files[expname] = [(fullname, ti_c)]
    for expname in output_files:  # sort all output_files by creation time
        output_files[expname].sort(key=lambda x: -x[1])
    return output_files


FullPath = str
CMDStr = str
Result = Union[str, float]


def get_outputs(output_filenames) -> Dict[FullPath, Dict[CMDStr, Result]]:
    outputs = {}
    for filename in output_filenames:
        # print(filename, ":")
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
                # STATUS.parse
                elif line.find('NaN') >= 0:
                    #    print("  NaN")
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = 'nan'
                        cur_st = READY
                elif line.find('Killed') >= 0:
                    #    print("  Killed")
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = 'killed'
                        cur_st = READY
                elif line.find('CUDA') >= 0:
                    #    print("  CUDA")
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = 'cudaerr'
                        cur_st = READY
                elif line.find('Error:') >= 0:
                    if cur_st == GOT_CMD:
                        outputs[filename][cur_cmd] = line
                        cur_st = READY
            # if cur_cmd == READY:
            #     outputs[filename][cur_cmd] = "Unknown error"
        # print(len(outputs[filename]))
    return outputs


def outputs_to_csv(logs1):
    # merge all outputs in different files
    all_outputs = []
    for i in logs1:
        all_outputs.append((i, logs1[i]['status'], logs1[i]['res']))
    # for i in outputs:
    #     all_outputs.extend(outputs[i].items())
    recognized_args = ['dataset', 'enc', 'dec', 'sampler', 'readout', 'est', 'dim', 'hiddens']
    csv_head = ','.join(recognized_args) + ',status,result,raw_cmd'
    csv_lines = []
    for cmd, status, res in all_outputs:
        if STATUS(status).is_unfinished():
            continue
        argsdict = CMD(cmd).argsdict
        args = []
        for arg in recognized_args:
            if arg not in argsdict:
                val = '-'
            else:
                val = argsdict[arg]
            args.append(val)
        csv_lines.append(
            ','.join(args) + ',' + str(status) + ',' + str(RES.fromdict(res).simple()).replace(',', ';') + ',' + cmd)
    csv_text = '\n'.join([csv_head] + csv_lines)
    csv_name = 'failure_analysis.csv'
    fullname = os.path.join(processed_dir, csv_name)
    with open(fullname, 'w') as fd:
        fd.write(csv_text)
    print(f"Wrote runtime failure analysis to {fullname}.")


def get_slurm_outputs(batch_path, base_name):
    all_files = True
    output_file_dict = search_output_files(batch_path, base_name,
                                           all_files=all_files)  # Dict[expname, List[Tuple[fullname, time]]]
    # print(list(itertools.chain(*output_file_dict.values())))
    output_filenames = {fullname for (fullname, _) in list(itertools.chain(*output_file_dict.values()))}
    outputs = get_outputs(output_filenames)
    return outputs, output_file_dict


def merge_outputs(outputs: Dict[FullPath, Dict[CMDStr, Result]], output_file_dict: Dict[Any, List[Tuple[str, float]]]) \
        -> Dict[Any, Dict[CMDStr, Result]]:
    # merge outputs; cover those earlier logs with older ones
    merged_outputs = {}  # Dict[expname, Dict[CMDStr, Result]]
    for expname in output_file_dict:
        merged_outputs[expname] = {}
        for fullname, _ in output_file_dict[expname]:  # already sorted latest to oldest
            if fullname in outputs:  # yes it is
                for cmd_str, res in outputs[fullname].items():
                    if cmd_str not in merged_outputs[expname]:  # write new to old without rewrite
                        merged_outputs[expname][cmd_str] = res
    return merged_outputs


def merge_outputs_2(outputs: Dict[FullPath, Dict[CMDStr, Result]], output_file_dict: Dict[Any, List[Tuple[str, float]]]) \
        :
    # merge outputs; cover those earlier logs with older ones
    merged_outputs = {}  # Dict[expname, Dict[CMDStr, Result]]
    merged_outputs2 = {}
    for expname in output_file_dict:
        merged_outputs[expname] = {}
        merged_outputs2[expname] = {}
        for fullname, ctime in output_file_dict[expname]:  # already sorted latest to oldest
            if fullname in outputs:  # yes it is
                for cmd_str, res in outputs[fullname].items():
                    if cmd_str not in merged_outputs[expname]:  # write new to old without rewrite
                        if not isinstance(res, str):
                            good_status = STATUS.FINISHED
                            good_result = RES.empty_res()
                            good_result['micro'] = res
                        else:
                            good_status = STATUS(res)
                            good_result = RES.empty_res()
                        good_exp = EXP(CMD(cmd_str), good_status, good_result, timestamp=ctime)
                        merged_outputs[expname][cmd_str] = res
                        merged_outputs2[expname][cmd_str] = good_exp
    return merged_outputs, merged_outputs2


def merge_progress_single(batch_cmd_single: list, finished_cmd_single: set, outputs_single: dict):
    res = {}
    for cmd in batch_cmd_single:
        if cmd in finished_cmd_single:
            res[cmd] = 1.  # random float
        elif cmd in outputs_single:
            res[cmd] = outputs_single[cmd]
        else:
            res[cmd] = 'unfinished'
    return res


# def merge_progress2(merged_outputs)

def merge_progress(merged_outputs, batch_cmd, finished_cmd):
    merged_progress = {}
    for expname in merged_outputs:
        batch_name = expname + '.sh'
        if batch_name in batch_cmd:
            merged_progress[expname] = merge_progress_single(batch_cmd[batch_name], finished_cmd[batch_name],
                                                             merged_outputs[expname])
    return merged_progress


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


# def remove_all_fakes():
#     ff

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
                exp = EXP.fromdict(cache_command[fd])
            else:
                exp = None
                try:
                    with open(os.path.join(path, fd), 'r') as f:
                        exp = EXP.fromlogfilehandler(f)
                        if exp is not None:
                            # print("??? EXP is NONE  !!!", fd)
                            # command = get_command(f)
                            # command, res = get_command_and_result(f)
                            new_logs[fd] = exp  # command

                            # if fd.find('fake') >= 0:
                            #     print("fake:", exp)
                except Exception as e:
                    raise e
                    print(e)
                    new_logs[fd] = None
            if exp is not None:
                logs.append(exp)
    except Exception as e:
        raise e
        print(e)
    return procnum, logs, new_logs


def search_logs(path):
    """
    Search for all log files in `path` and extract their cmd info.
    @param path: path to log files.
    @return: a set of all cmd strings.
    """
    files = os.listdir(path)  # all files (not necessarily log files)
    # files.sort()  # sort later

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
    # print("back on earth")
    # this is why we pass procnum into `get_logs_from_file_list`:
    # Pool.imap_unordered returns a list of results in random order
    # so we must restore order through a sort
    # Recall that `get_logs_from...` returns [procnum, logs, new_logs]
    # ret_list.sort(key=lambda x: x[0])
    all_commands = []
    all_new_cmds = {}

    for k in range(n_split):
        all_commands.extend(ret_list[k][1])
        all_new_cmds.update(ret_list[k][2])
    # print("allnew")
    # print(all_new_cmds)
    # with open(os.path.join(processed_dir, 'weird.txt'), 'w') as fd:
    #     print("all new commands", file=fd)
    #     print(all_commands, file=fd)
    #     print("finished", file=fd, flush=True)
    cache.write_cmd(all_new_cmds)

    # get logs from cache in case they are from .othermonitorcache.json
    all_commands = list(cache.get_cmd().items())
    all_commands.sort(key=lambda x: x[0], reverse=True)
    print("hello")
    # remove duplicate cmd
    new_commands = []
    command_set = set()
    for i in range(len(all_commands)):
        _, exp = all_commands[i]
        if exp['cmd'] not in command_set:
            command_set.add(exp['cmd'])
            # simpliest way to add fake experiments here
            # if exp['status'] == STATUS.FINISHED:
            new_commands.append(exp)

    log(f'Found {len([exp for exp in new_commands if exp["status"] == STATUS.FINISHED])} experiments.')
    return new_commands


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


def get_CMD(filenames) -> Dict[str, List[CMD]]:
    """
    Get all cmd lines in a list of batch files.

    call `get_files` first, and normalize each cmd line.
    @param filenames: a list of files (full path)
    @return:
    """
    r1 = get_files(filenames)
    ret = {}
    for file, val in r1.items():
        ret[os.path.basename(file)] = [CMD(x) for x in val if iscmd(x)]
    return ret


def check_progress(batch_cmd: Dict[str, List], logs: Set) \
        -> (Dict[str, Set], Dict[str, Tuple[int]]):
    finished_cmd = {}
    finished_ratio = {}
    # print(logs)
    logs = set(str(x) for x in logs)
    # print("___")
    for batch_file in batch_cmd:
        # print(batch_cmd[batch_file])
        finished_cmd[batch_file] = logs.intersection(batch_cmd[batch_file])
        finished_ratio[batch_file] = (len(finished_cmd[batch_file]), len(batch_cmd[batch_file]))

    return finished_cmd, finished_ratio


def get_unfinished(batch_cmd: Dict[str, Iterable], finished_cmd: Dict[str, Iterable]) \
        -> Dict[str, set]:
    unfinished_cmd = {}
    for batch_file in batch_cmd:
        unfinished_cmd[batch_file] = set(batch_cmd[batch_file]).difference(finished_cmd[batch_file])

    return unfinished_cmd


def read_files(batch_path, base_name, log_path, do_search_logs=True, mode='leaf'):
    batch_files = search_batch_files(batch_path, base_name, mode=mode)
    #    print(batch_files)
    batch_cmd = get_cmd(batch_files)
    if do_search_logs:
        logs = search_logs(log_path)
    else:
        logs = None
    return batch_cmd, logs


def show_batch_info(batch_files, batch_info, running_jobs=None, title=None, title_description=None, hierarchical=False):
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
    batch_files_sorted.sort(key=lambda x: x.replace('.sh', ''))
    # batch_files_sorted.sort(key=lambda x: '0' + x.replace('.sh','') if x in running_jobs else '1' + x.replace('.sh',''))
    set_batch_files = set(x.replace('.sh', '') for x in batch_files)
    starting_chars = {}

    for batch_file in batch_files_sorted:
        if batch_file in running_jobs:
            begin_color = highlight_color
            end_color = default_color
            description = f"(ID {running_jobs[batch_file].jobid})"
        else:
            begin_color = ""
            end_color = ""
            description = ""
        starting_chars[batch_file] = ''
        if hierarchical:
            father = prefix_of(set_batch_files, batch_file.replace('.sh', ''), self_contain=False, longest=True)
            # print(f"batch_file {batch_file}, father {father}")
            if father:
                starting_chars[batch_file] = starting_chars[father + '.sh'] + '\t'
                batch_info[batch_file] = batch_info[batch_file].replace('\n', '\n' + starting_chars[batch_file])
        print(
            f"{starting_chars[batch_file]}{begin_color}{batch_file}{end_color}{description}: {batch_info[batch_file]}")
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
    logs = set(exp['cmd'] for exp in logs if exp['status'] == STATUS.FINISHED)

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


def check_outputs(batch_path, base_name, log_path, mode='leaf'):
    r_base_name = ['R-' + name for name in base_name]
    outputs, output_file_dict = get_slurm_outputs(batch_path, r_base_name)

    merged_outputs, merged_outputs2 = merge_outputs_2(outputs, output_file_dict)
    output_status_table = {}
    for expname in merged_outputs2:
        EXP.merge_exp_table(output_status_table, merged_outputs2[expname])
    # print(output_status_table)
    cache.write_status_table(output_status_table)
    batch_cmd, logs = read_files(batch_path, base_name, log_path, mode=mode)
    logs1 = set(exp['cmd'] for exp in logs if exp['status'] == STATUS.FINISHED)
    finished_cmd, finished_ratio = check_progress(batch_cmd, logs1)
    # merged_progress = merge_progress(merged_outputs, batch_cmd, finished_cmd)
    logs1 = {exp['cmd']: exp for exp in logs}
    EXP.merge_exp_table(logs1, cache.get_status_table())
    merged_progress = {}
    for batch_file in batch_cmd:
        expname = batch_file.replace('.sh', '')
        merged_progress[expname] = {}
        cmd_set = set(batch_cmd[batch_file])
        for cmd in cmd_set:
            if cmd in logs1:
                merged_progress[expname][cmd] = logs1[cmd]  # ['status']
            else:
                merged_progress[expname][cmd] = EXP(CMD(cmd), STATUS.UNFINISHED)

    return outputs, output_file_dict, batch_cmd, logs1, finished_cmd, finished_ratio, merged_progress


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


def refresh_exps(batch_path, base_name, log_path, running_jobs=None, display=True, failure_args=None, **kwargs):
    outputs, output_file_dict, batch_cmd, logs1, finished_cmd, finished_ratio, merged_progress = check_outputs(
        batch_path, base_name, log_path, mode='leaf')
    if kwargs.get('rerun', False):
        new_exps: Dict[str, set] = {k: set(v) for k, v in batch_cmd.items()}
        # write fake exps
        if kwargs.get('hard', False):
            print("Covering old files...")
            cmdstrs = list(set(itertools.chain(*new_exps.values())))
            for cmdstr in tqdm.tqdm(cmdstrs):
                if cmdstr in logs1 and logs1[cmdstr]['status'] != STATUS.UNFINISHED:
                    EXP.fakelogfile(cmdstr)
    else:
        unfinished = get_unfinished(batch_cmd, finished_cmd)

        # combine failure args
        new_exps = unfinished
    print("kwargs:", kwargs)
    # for filter_arg_set in kwargs['filter']:  # 'or'
    #     print("set", filter_arg_set)
    #     for filter_arg in filter_arg_set.split('+'):  # 'and'
    #         print("  arg:", filter_arg)
    filter_exps = new_exps
    if 'filter' in kwargs:
        old_exps = filter_exps
        filter_exps = {}
        for batch_file in old_exps:
            filter_exps[batch_file] = set()
            for cmd in old_exps[batch_file]:
                keep = False
                for filter_arg_set in kwargs['filter']:  # 'or'
                    meet = True
                    for filter_arg in filter_arg_set.split('+'):  # 'and'
                        if cmd.find(filter_arg) < 0:
                            meet = False
                            break
                    if meet:
                        keep = True
                        break
                if keep:
                    filter_exps[batch_file].add(cmd)

    # failure args
    failure_exps = new_exps
    if failure_args is not None:
        # print("failure_args")
        if failure_args.fail and failure_args.killed and failure_args.nan and failure_args.cudaerr \
                and failure_args.finished and failure_args.unfinished and failure_args.others:
            failure_args = None
        #     print("None")
    if failure_args is not None:

        # outputs, output_file_dict = get_slurm_outputs(batch_path, r_base_name)
        for batch_file in batch_cmd:
            exp_name = os.path.basename(batch_file).replace('.sh', '')
            if exp_name in merged_progress:
                output_info: Dict[str, STATUS] = {k: STATUS(v['status']) for k, v in merged_progress[exp_name].items()}
                for cmd in output_info:
                    if cmd not in failure_exps[batch_file]:
                        continue
                    if not failure_args.fail:
                        if output_info[cmd].is_failed():
                            failure_exps[batch_file].remove(cmd)
                    else:
                        if not failure_args.killed:
                            if output_info[cmd].is_killed():
                                failure_exps[batch_file].remove(cmd)
                        if not failure_args.nan:
                            if output_info[cmd].is_nan():
                                failure_exps[batch_file].remove(cmd)
                        if not failure_args.cudaerr:
                            if output_info[cmd].is_cudaerr():
                                failure_exps[batch_file].remove(cmd)
                        if not failure_args.others:
                            if output_info[cmd].is_others():
                                failure_exps[batch_file].remove(cmd)
                    if not failure_args.finished:
                        if output_info[cmd].is_finished():
                            failure_exps[batch_file].remove(cmd)
                    if not failure_args.unfinished:
                        if output_info[cmd].is_unfinished():
                            failure_exps[batch_file].remove(cmd)

    # merge failure exps and filter exps
    new_exps = {}
    or_sign = kwargs.get('filter_or_flags', False)
    for batch_file in batch_cmd:
        if or_sign:  # OR, merge
            new_exps[batch_file] = failure_exps[batch_file].union(filter_exps[batch_file])
        else:
            new_exps[batch_file] = failure_exps[batch_file].intersection(filter_exps[batch_file])

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


class JobBlockManager(Iterable):
    def __init__(self, it: Iterable[JobBlock]):
        self.jobs = {job.name: job for job in it}

    def __contains__(self, item):
        return item in self.jobs

    def __iter__(self):
        return self.jobs

    def __getitem__(self, item) -> JobBlock:
        return self.jobs[item]

    def __len__(self):
        return len(self.jobs)


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
    failure_args = parse_failure_args(args)
    jobs = get_running_jobs()
    refresh_exps(batch_path, base_name, log_path, jobs,
                 failure_args=failure_args,
                 rerun=args.rerun, filter=args.filter,
                 filter_or_flags=args.filter_or_flags,
                 hard=args.hard)


def run_job_sbatch(name, partition, sbatch_args=None):
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

    cmd_args = {'-G': '1', '-p': partition}
    raw_s_args = [x for x in sbatch_args.split(' ') if x]
    for i in range(0, len(raw_s_args), 2):
        cmd_args[raw_s_args[i]] = raw_s_args[i + 1]
    print(f"run {name} at {os.path.abspath(os.curdir)} with partition {cmd_args['-p']} and args {sbatch_args}")
    cmd_args = list(itertools.chain(*cmd_args.items()))
    output = subprocess.check_output(['sbatch', *cmd_args, '--output=R-%x.%j.out', name]).decode('utf-8')
    print(output)
    os.chdir(tmpdir)
    return output.strip().split(' ')[-1]  # job id
    # subprocess.run(['sbatch', '-G', '1', '-p', partition, name])


def stop_job_sbatch(name, jobid):
    print(f"stop {name} (jobid: {jobid})")
    subprocess.run(['scancel', jobid])


def run_batch_files(batch_file_names, partitions, sbatch_args=''):
    for name in batch_file_names:
        run_job_sbatch(name, partitions[0], sbatch_args)


def stop_batch_files(batch_file_names: Iterable[FullPath], jobs):
    for name in batch_file_names:
        if os.path.basename(name) in jobs:
            stop_job_sbatch(name, jobs[os.path.basename(name)].jobid)


def parse_failure_args(args):
    class Tmp:
        def __init__(self):
            self.nan = True
            self.killed = True
            self.fail = True
            self.cudaerr = True
            self.finished = True
            self.unfinished = True
            self.others = True

    ret = Tmp()
    attrs = ['nan', 'killed', 'fail', 'cudaerr', 'finished', 'unfinished', 'others']
    for attr in attrs:
        setattr(ret, attr, getattr(args, attr, True))
    return ret


daemon_list = Path(os.path.join(processed_dir, 'daemon.list'))
daemon_list.touch(exist_ok=True)


def get_daemon_set():
    while True:
        try:
            with open(daemon_list, 'r') as fd:
                daemons = set(x.strip() for x in fd)
                return set(daemons)
        except IOError:
            continue


def get_daemon_status(pid):
    status_file = os.path.join(processed_dir, f'daemon-{pid}.status')
    while True:
        try:
            with open(status_file, 'r') as fd:
                return json.load(fd)
        except FileNotFoundError:
            print("Status file does not exist.")
            return None
        except IOError:
            continue
        except json.JSONDecodeError:
            print("Status file corrupted.")
            return None


def parse_daemon(args):
    daemons = get_daemon_set()
    if args.pid is not None:
        status_file = os.path.join(processed_dir, f'daemon-{args.pid}.status')
        if args.pid not in daemons:
            if not os.path.exists(status_file):
                print("Daemon does not exist.")
                return
            else:
                print("Daemon is not running.")
        else:
            print("Daemon is running.")
        if args.call is None:
            print(f"Status of {args.pid}:")
            status = get_daemon_status(args.pid)
            if status:
                # print(status)
                for k, v in status.items():
                    if not v:
                        v = 'None'
                    if len(k) > 20:
                        print(k, ":")

                        if isinstance(v, list):
                            for pv in v:
                                if os.path.isfile(pv):
                                    pv = os.path.basename(pv)
                                print(' ' * 22 + str(pv))
                        elif isinstance(v, dict):
                            for pv in v:
                                if os.path.isfile(pv):
                                    pv1 = os.path.basename(pv)
                                print(' ' * 22 + f'{pv1}: {v[pv].strip()}')
                        else:
                            print(' ' * 22 + str(v))
                    else:
                        print('{:22}'.format(k + ':'), end='')
                        if isinstance(v, list):
                            for i, pv in enumerate(v):
                                if os.path.isfile(pv):
                                    pv = os.path.basename(pv)
                                if i == 0:
                                    print(str(pv).strip())
                                else:
                                    print(' ' * 22 + str(pv).strip())
                        elif isinstance(v, dict):
                            for i, pv in enumerate(v):
                                if os.path.isfile(pv):
                                    pv1 = os.path.basename(pv)
                                if i == 0:
                                    print(f'{pv1}: {v[pv].strip()}')
                                else:
                                    print(' ' * 22 + f'{pv1}: {v[pv].strip()}')
                        else:
                            print(str(v))
        else:
            pid = args.pid
            input_file = os.path.join(processed_dir, f'daemon-{pid}.in')
            output_file = os.path.join(processed_dir, f'daemon-{pid}.out')
            hash_id = random.randint(0, 65535)
            mail = json.dumps({"hash": hash_id, "content": args.call})
            while True:
                try:
                    with open(input_file, 'a') as fd:
                        fd.write(mail + '\n')
                    break
                except IOError:
                    continue
            # wait for response
            time_start = time()
            ls = []
            while time() - time_start < 3:
                try:
                    with open(output_file, 'r') as fd:
                        ls = fd.readlines()
                    flg = 0
                    for line in ls:
                        m1 = json.loads(line)
                        if m1['hash'] == hash_id:
                            print(f"Response from daemon: {m1['content']}")
                            flg = 1
                            break
                    if flg:
                        break
                except IOError:
                    continue


    else:
        print("Running daemons:", ' '.join(daemons))


def start_daemon(batch_file_names, partitions, sbatch_args):
    curdir = os.path.abspath(os.curdir)

    def begin_print():
        print('\r' + ' ' * 99 + '\r', end='', file=sys.stderr)

    user = getpass.getuser()
    hostname = socket.gethostname()
    green = "\033[32m\033[1m"
    blue = "\033[34m\033[1m"
    white = "\033[0m"

    def end_print():
        print(green + user + '@' + hostname + white + ':' + blue + curdir + white + '$', end=' ', file=sys.stderr,
              flush=True)
        print(flush=True)

    with daemon.DaemonContext(stderr=sys.stderr):
        pid = os.getpid()

        input_file = os.path.join(processed_dir, f'daemon-{pid}.in')
        output_file = os.path.join(processed_dir, f'daemon-{pid}.out')
        log_file = os.path.join(processed_dir, f'daemon-{pid}.log')
        status_file = os.path.join(processed_dir, f'daemon-{pid}.status')
        status = {'pid': pid, 'daemon_status': 'preparing',
                  'running_jobs': {}, 'finished_jobs': [],
                  'ready_jobs': {}, 'pending_jobs': list(batch_file_names),
                  'killed_jobs': []}

        with open(input_file, 'w') as fd:
            fd.write('')
        with open(output_file, 'w') as fd:
            fd.write('')

        def read_input():
            while True:
                try:
                    with open(input_file, 'r') as fd:
                        lines = fd.readlines()
                    # clear input
                    with open(input_file, 'w') as fd:
                        fd.write('')
                    break
                except IOError:
                    continue
            return lines

        def write_output(*a, **k):
            while True:
                try:
                    with open(output_file, 'w') as fd:
                        print(*a, file=fd, **k)
                    break
                except IOError:
                    continue

        def write_log(*a, **k):
            while True:
                try:
                    with open(log_file, 'a') as fd:
                        print(f'[{str(datetime.datetime.now())}] ', *a, file=fd, **k)
                    break
                except IOError:
                    continue

        def write_status():
            while True:
                try:
                    with open(status_file, 'w') as fd:
                        json.dump(status, fd)
                    break
                except IOError:
                    continue

        write_status()
        while True:  # wait for daemon_list
            try:
                with open(daemon_list, 'r') as fd:
                    daemons = set(i.strip() for i in fd)
                daemons.add(str(pid))
                with open(daemon_list, 'w') as fd:
                    for i in daemons:
                        fd.write(i + '\n')
                break
            except IOError:
                continue
        begin_print()
        print(f"New daemon: {pid}", file=sys.stderr)
        print(file=sys.stderr)
        print("Running daemons:", ' '.join(daemons), file=sys.stderr)
        print(file=sys.stderr)
        print("You can use the following command to check daemons:", file=sys.stderr)
        print(file=sys.stderr)
        print("python monitor.py daemon", file=sys.stderr)
        print(f"python monitor.py daemon --pid {pid}", file=sys.stderr)
        print(file=sys.stderr)
        end_print()

        status['daemon_status'] = 'running'
        write_status()
        write_log('Start running.')
        mails_out = []
        try:
            while True:  # real loop
                if status['daemon_status'] == 'stopping':
                    while True:  # wait for daemon_list
                        try:
                            with open(daemon_list, 'r') as fd:
                                daemons = set(i.strip() for i in fd)
                            daemons.remove(str(pid))
                            with open(daemon_list, 'w') as fd:
                                for i in daemons:
                                    fd.write(i + '\n')
                            break
                        except IOError:
                            continue
                    status['daemon_status'] = 'finished'
                    write_status()
                    exit(0)
                write_log("I'm alive.")
                jobs = get_running_jobs()
                # update running jobs

                for filename in status['ready_jobs']:
                    jobname = os.path.basename(filename)
                    if jobname in jobs and jobs[jobname].jobid == status['ready_jobs'][filename]:
                        status['running_jobs'][filename] = status['ready_jobs'][filename]
                        write_log(filename, 'started')

                for filename in status['running_jobs']:
                    if filename in status['ready_jobs']:
                        status['ready_jobs'].pop(filename)

                stopped_jobs = []

                for filename in status['running_jobs']:
                    jobname = os.path.basename(filename)
                    if jobname not in jobs or jobs[jobname].jobid != status['running_jobs'][filename]:
                        stopped_jobs.append(filename)
                for filename in stopped_jobs:
                    status['running_jobs'].pop(filename)
                    status['finished_jobs'].append(filename)
                    write_log(filename, 'finished')

                if len(jobs) < args.max_job_num:
                    # get files to run
                    new_jobs = 0
                    while new_jobs + len(jobs) < args.max_job_num and len(status['pending_jobs']) > 0:
                        new_jobs += 1
                        filename = status['pending_jobs'][0]
                        # start new job
                        jobid = run_job_sbatch(filename, partitions[0], sbatch_args)
                        status['pending_jobs'].pop(0)
                        status['ready_jobs'][filename] = jobid
                        write_log(filename, f'applied jobid {jobid}')

                write_status()

                if len(status['pending_jobs']) == 0 and len(status['ready_jobs']) == 0 and len(
                        status['running_jobs']) == 0:
                    # end
                    status['daemon_status'] = 'stopping'
                    write_status()
                    hello_message = f'Daemon {pid} has done its job.'
                else:
                    hello_message = f'Hi from daemon {pid}!'

                def mail_write(query_hash, content):
                    write_log("writing output:", content)
                    if len(mails_out) > 20:
                        mails_out.pop(0)
                    mails_out.append(json.dumps({'hash': query_hash, 'content': content}))
                    contents = '\n'.join(mails_out)
                    write_log("writing output:", contents)
                    write_output(contents)

                # get input
                inputs = read_input()
                write_log(f'{len(inputs)} inputs')
                for query in inputs:
                    try:
                        query = json.loads(query)
                    except json.JSONDecodeError:
                        continue  # no respond
                    if not isinstance(query, dict):
                        continue  # no respond
                    if 'hash' not in query:
                        continue  # no respond
                    write_log(f'{query}: adequate')
                    if 'content' not in query:
                        mail_write(query['hash'], 'No content!')
                    elif query['content'] == 'hello':
                        mail_write(query['hash'], hello_message)
                    elif query['content'] == 'kill':
                        mail_write(query['hash'], 'ready to end.')
                        # kill jobs
                        for job in status['running_jobs']:
                            stop_job_sbatch(job, status['running_jobs'][job])
                        for job in status['ready_jobs']:
                            stop_job_sbatch(job, status['ready_jobs'][job])
                        status['killed_jobs'] = status['running_jobs']
                        status['killed_jobs'].update(status['ready_jobs'])
                        status['running_jobs'] = status['ready_jobs'] = {}
                        status['daemon_status'] = 'stopping'
                        write_status()
                    else:
                        mail_write(query['hash'], hello_message)
                sleep(0.04)
        except Exception:
            status['daemon_status'] = 'stopping'


def parse_run(args):
    batch_path, base_name, log_path = parse_common_args(args)
    failure_args = parse_failure_args(args)
    sbatch_args = args.sbatch_args
    jobs = get_running_jobs()
    partitions = get_partition()
    if len(partitions) == 0:
        print("No partitions available!")
        exit(1)

    #  update experiment
    batch_file_names = refresh_exps(batch_path, base_name, log_path, jobs, failure_args=failure_args,
                                    rerun=args.rerun, filter=args.filter, filter_or_flags=args.filter_or_flags,
                                    hard=args.hard)

    #  do not update
    # batch_file_names = search_batch_files(batch_path, base_name)
    # for name in batch_file_names:
    #     if os.path.basename(name) not in jobs:
    #         run_job_sbatch(name, partitions[0])
    if args.keep_current is False:
        all_batch_file_names = search_batch_files(batch_path, base_name, 'all')
        stop_batch_files(all_batch_file_names, jobs)

    if args.max_job_num == -1:
        run_batch_files(batch_file_names, partitions, sbatch_args)
    else:  # daemon mode

        start_daemon(batch_file_names, partitions, sbatch_args)


def parse_stop(args):
    batch_path, base_name, log_path = parse_common_args(args)
    jobs = get_running_jobs()

    batch_file_names = search_batch_files(batch_path, base_name, 'all')
    stop_batch_files(batch_file_names, jobs)


def get_output_status(output_info, count_finished=True):
    error_dict = {}
    for _, res in output_info.items():
        if str(res) == '1.0':
            res = 'finished'
        error_dict[str(res)] = error_dict.get(str(res), 0) + 1
    if not count_finished and 'finished' in error_dict:
        error_dict.pop('finished')
    sorted_items = list(error_dict.items())
    sorted_items.sort(key=lambda x: x[0])
    return ', '.join(f'{cnt} {res}' for res, cnt in sorted_items)


def parse_check(args):
    batch_path, base_name, log_path = parse_common_args(args)
    if args.long:
        mode = 'all'
    else:
        mode = 'root'
    outputs, output_file_dict, batch_cmd, logs1, finished_cmd, finished_ratio, merged_progress = check_outputs(
        batch_path, base_name, log_path, mode=mode)

    last_run_batch_cmd, _ = read_files(output_dir, base_name, log_path, False)
    jobs = get_running_jobs()
    # display

    title = 'Runtime Analysis'
    batch_files = list(batch_cmd.keys())
    batch_info = {}
    for batch_file in batch_files:

        finished_str = f'{finished_ratio[batch_file][0]}' \
                       f'/{finished_ratio[batch_file][1]}' \
                       f' finished'
        exp_name = os.path.basename(batch_file).replace('.sh', '')
        # print(exp_name)
        if exp_name in merged_progress:
            # all runs
            output_info = {k: v['status'] for k, v in merged_progress[exp_name].items()}
            run_status_str = get_output_status(output_info, count_finished=False)
            if run_status_str:
                run_status_str = ', ' + run_status_str

            # last run, legacy code
            if exp_name in output_file_dict:

                last_run_output_file_name, _ = output_file_dict[exp_name][0]
                _, jobid = parse_output_name(last_run_output_file_name)

                output_info = outputs[last_run_output_file_name]
                # if len(output_info) < 2:
                #    print(exp_name, output_info)
                batchname = exp_name + '.sh'
                if batchname not in last_run_batch_cmd or batchname not in finished_cmd:
                    last_run_str = ''
                else:
                    last_run_str = get_output_status(
                        merge_progress_single(last_run_batch_cmd[batchname], finished_cmd[batchname], output_info))
                if args.last_run:
                    if last_run_str:
                        last_run_str = f'\n last run (ID {jobid}): ' + last_run_str
                    else:
                        last_run_str = f'\n last run (ID {jobid})'
                else:
                    last_run_str = f' (last run ID {jobid})'
                batch_info[batch_file] = finished_str + run_status_str + last_run_str
            else:
                batch_info[batch_file] = finished_str + run_status_str
        else:
            batch_info[batch_file] = finished_str
    show_batch_info(batch_files, batch_info, jobs, title, hierarchical=args.long)
    outputs_to_csv(logs1)
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


def receive_data(socket, silent=False):
    def log(*args, **kwargs):
        if not silent:
            print(*args, **kwargs)

    data = b''
    exitflag = False
    while not exitflag:
        block = socket.recv(blocksize)
        data += block
        if data.endswith(endingbytes):
            exitflag = True
            data = data.replace(endingbytes, b'')

        log(clearline, end='')
        log(f"({len(data)} bytes received.)", end='', flush=True)
    log(f"(All received.)", flush=True)
    # print(data.decode('utf-8')[-200:])
    return data


def send_data(socket, data, silent=False):
    def log(*args, **kwargs):
        if not silent:
            print(*args, **kwargs)

    log(f"({len(data)} bytes to send...)")
    # print(data.decode('utf-8')[-200:])
    for i in range(0, len(data), blocksize):
        socket.sendall(data[i:i + blocksize])
        log(clearline, end='')
        log(f"({i + len(data[i:i + blocksize])} bytes sent.)", end='', flush=True)
    socket.sendall(endingbytes)
    log(f"(All sent.)", flush=True)


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


def parse_send(args):
    print(f"local IPv4: {HOST}")
    if args.server == 'self':
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print("Waiting for connection. "
                  "Use the following command on another server to send data here:")
            print()
            print(f"python monitor.py send --server {HOST} --file FILENAME")
            print()
            args.dest = os.path.abspath(os.path.normpath(args.dest))
            print(f"Files will be stored in {args.dest}")
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr}.')
                name = receive_data(conn).decode('utf-8')
                data = receive_data(conn)
                with open(os.path.join(args.dest, name), 'wb') as fd:
                    fd.write(data)
                print(f"Received {name}.")
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            with open(args.file, 'rb') as fd:
                content = b''
                while True:
                    block = fd.read(blocksize)
                    if block:
                        content += block
                    else:
                        break
            print("Connecting...")
            s.connect((args.server, PORT))
            print(f"Connected to {args.server}.")
            send_data(s, os.path.basename(args.file).encode('utf-8'))
            send_data(s, content)
            print(f"Sent {args.file}.")


parser = ArgumentParser()
subparsers = parser.add_subparsers()
parser_show = subparsers.add_parser('show', help='Show experiment progress.')
parser_gen = subparsers.add_parser('gen', help='Generate new experiment settings.')
parser_run = subparsers.add_parser('run', help='Run experiments.')
parser_stop = subparsers.add_parser('stop', help='Stop experiments.')
parser_sync = subparsers.add_parser('sync', help='Sync between multiple servers.')
parser_check = subparsers.add_parser('check', help='Check experiment status.')
parser_daemon = subparsers.add_parser('daemon', help='...')
for parserx in [parser_show, parser_gen, parser_run, parser_stop, parser_check]:
    parserx.add_argument('--base', default='autogen_sample_script_', help='Provide base name for autogen script.')
    parserx.add_argument('--range', '-r', nargs='*', default=[''],
                         help='Select process range for autogen script.')
    parserx.add_argument('--srcdir', default=src_dir, help='Path to autogen script.')
    parserx.add_argument('--logdir', default=log_dir, help='Path to logs.')
    parserx.add_argument('--long', '-l', action='store_true', help='Print long info.')
parser_sync.add_argument('--server', default='self', help='Address of server. By default this machine will be server.')
parser_send = subparsers.add_parser('send', help='Send files between multiple servers.')
parser_send.add_argument('--server', default='self', help='Address of server. By default this machine will be server.')
parser_send.add_argument('--file', default=cache.cachefile, help='Client: select file to send.')
parser_send.add_argument('--dest', default=output_dir,
                         help=f'Server: select where to store. By default, files are stored in {output_dir}.')

parser_run.add_argument('--sbatch-args', default='',
                        help='Control sbatch args. For example, --sbatch-args "--mem 50G".')
for parserx in [parser_gen, parser_run]:
    parserx.add_argument('--rerun', '-R', action='store_true',
                         help='Rerun all experiments that meet your requirements.')
    parserx.add_argument('--hard', '-H', action='store_true',
                         help='Works with rerun. Disable past experiments (be careful).')
    parserx.add_argument('--filter', nargs='*', default=[''],
                         help='Provide experiment filters. Only those experiments that contain all filters are run.'
                              '\nFilters go like "cora+dgi pubmed+mvgrl", with ANDs provided with + and ORs provided with whitespace.')
    parserx.add_argument('--no-nan', action='store_false', dest='nan',
                         help='Do not run experiments that have produced NaN.')
    parserx.add_argument('--no-killed', action='store_false', dest='killed',
                         help='Do not run experiments that are killed by slurm.')
    parserx.add_argument('--no-fail', action='store_false', dest='fail',
                         help='Do not run experiments that have failed.')
    parserx.add_argument('--no-cudaerr', action='store_false', dest='cudaerr',
                         help='Do not run experiments that have cuda errors.')
    parserx.add_argument('--no-finished', action='store_false', dest='finished',
                         help='Do not run (successfully) finished experiments.')
    parserx.add_argument('--no-unfinished', action='store_false', dest='unfinished',
                         help='Do not run unfinished experiments (i.e. those which have never been run).')
    parserx.add_argument('--no-others', action='store_false', dest='others',
                         help='Do not run experiments with other errors.')
    parserx.add_argument('--filter-or-flags', action='store_true',
                         help='By default we apply filter AND the `--no-xxx` flags. Set this '
                              'to apply filter OR the flags.')
parser_run.add_argument('--keep-current', action='store_true',
                        help='This keeps current running experiments IN RANGE. '
                             'By default, these are killed at each new monitor run.')
parser_run.add_argument('--daemon', '-d', nargs='?', type=int, dest='max_job_num', const=999, default=-1,
                        help='Enter daemon mode. In this mode, monitor will create a daemon'
                             'to guard your running processes. The daemon tries'
                             'to keep `max_job_num` (or unlimited, if you do not set the value)'
                             ' running jobs. It ends when all jobs'
                             'in range are finished.')
parser_daemon.add_argument('--pid', default=None)
parser_daemon.add_argument('--call', default=None)

parser_check.add_argument('--last-run', '-L', action='store_true', help='Print info about last run.')
parser_show.set_defaults(func=parse_show)
parser_gen.set_defaults(func=parse_gen)
parser_run.set_defaults(func=parse_run)
parser_stop.set_defaults(func=parse_stop)
parser_sync.set_defaults(func=parse_sync)
parser_check.set_defaults(func=parse_check)
parser_send.set_defaults(func=parse_send)
parser_daemon.set_defaults(func=parse_daemon)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
    cache.close()
