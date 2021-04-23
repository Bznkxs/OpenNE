"""
monitor
"""

from argparse import ArgumentParser
import os
import sys
from multiprocessing import Pool
import subprocess
import re

from typing import Dict, List, Set, Iterable, Sized, Tuple

import tqdm

cur_dir = os.path.dirname(__file__)
root_dir = os.path.normpath(os.path.join(cur_dir, '..', '..'))
src_dir = os.path.join(root_dir, 'src')
log_dir = os.path.join(src_dir, 'logs')
output_dir = os.path.normpath(os.path.join(cur_dir, '..', 'processed', 'output'))
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


class CMD:
    def __init__(self, cmd_str: str):
        self.args = cmd_str.replace('$*', '').strip().replace('  ', ' ').split('--')
        self.args.sort()
        self.sorted_cmd_str = '--'.join(self.args)

    def __str__(self):
        return self.sorted_cmd_str

    def __repr__(self):
        return self.sorted_cmd_str

    def __hash__(self):
        return hash(self.sorted_cmd_str)


def normalcmd(cmd):
    return CMD(cmd).sorted_cmd_str


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
    files_iter = os.listdir(path)

    batch_file_tree = {}

    for fd in files_iter:
        if fd.endswith('.sh') and fd.startswith(base_name):
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


def search_batch_files(path, base_name):
    """
    keeps only the 'leaf files' in `path` with prefix `base_name` and suffix '.sh'
    e.g. if we have enc.sh, enc_0.sh, enc_1.sh, this will return the latter two files
    @param path:
    @param base_name:
    @return: a list of files
    """
    files_iter = os.listdir(path)

    batch_files = set()

    def prefix_of(filename: str):
        """
        @param filename: file name to put into batch_files
        @return: file name in batch_files that is prefix of `filename`
        """
        for file in batch_files:
            if filename.startswith(file):
                return file
        return None

    def has_prefix(filename: str):
        """
        @param filename: file name to put into batch_files
        @return: file name in batch_files that has prefix `filename`
        """
        for file in batch_files:
            if file.startswith(filename):
                return file
        return None

    def remove(filename: str):
        """
        @param filename: file name to remove from batch_files
        @return: None
        """
        batch_files.remove(filename)

    def add(filename: str):
        """
        @param filename: file name to add to batch_files
        @return: None
        """
        batch_files.add(filename)

    for fd in files_iter:
        if fd.endswith('.sh') and fd.startswith(base_name):
            fd = fd.rstrip('.sh')
            prefix = prefix_of(fd)
            if prefix is not None:
                remove(prefix)
            child = has_prefix(fd)
            if child is None:
                add(fd)

    ret = []
    for fd in batch_files:
        ret.append(os.path.join(path, fd + '.sh'))
    return ret


def warn(e):
    # print(e)
    pass


def log(*args, **kwargs):
    print(*args, **kwargs)


def get_command(f):
    for pline in f:
        if pline.startswith('python'):  # recognized as command
            return normalcmd(pline)
    return None


def get_logs_from_file_list(arg):
    procnum, path, files_iter = arg
    logs = []
    try:
        for ni, fd in enumerate(files_iter):
            command = None
            try:
                with open(os.path.join(path, fd), 'r') as f:
                    command = get_command(f)
            except Exception as e:
                warn(e)
            if command is not None:
                logs.append(command)
    except Exception as e:
        print(e)
    return procnum, logs


def ddd(arg):
    proc, _, _ = arg
    return proc, []


def search_logs(path):
    files = os.listdir(path)
    files.sort()  # so it is sorted by time
    n_split = 100

    n_files = len(files)
    sub_size = (n_files + n_split - 1) // n_split
    split_files = [(i, path, files[i * sub_size: (i + 1) * sub_size]) for i in range(n_split)]

    log("Searching for logs...")
    ret_list = []
    with Pool(n_split) as p:
        for whatever_x in tqdm.tqdm(p.imap_unordered(get_logs_from_file_list, split_files), total=n_split):
            ret_list.append(whatever_x)
    ret_list.sort(key=lambda x: x[0])
    all_commands = []
    for k in range(n_split):
        all_commands.extend(ret_list[k][1])
    log(f'Found {len(set(all_commands))} logs.')
    return set(all_commands)


def get_files(filenames) -> Dict[str, List[str]]:
    """
    read files and put list of lines in dict
    @param filenames: list of files
    @return: dict of lists
    """
    ret = {}
    for file in filenames:
        ret[file] = list(open(file, 'r'))
    return ret


def get_cmd(filenames) -> Dict[str, List[str]]:
    r1 = get_files(filenames)
    ret = {}
    for file, val in r1.items():
        ret[os.path.basename(file)] = [normalcmd(x) for x in val]
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
        unfinished_cmd[batch_file] = set(batch_cmd[batch_file]).difference(finished_cmd)

    return unfinished_cmd


def read_files(batch_path, base_name, log_path):
    batch_files = search_batch_files(batch_path, base_name)
    batch_cmd = get_cmd(batch_files)
    logs = search_logs(log_path)
    return batch_cmd, logs


def show_batch_info(batch_files, batch_info, running_jobs=None, title=None):
    if running_jobs is None:
        running_jobs = {}
    if title is None:
        title = "Batch info"
    running_jobs = {job.name: job for job in running_jobs}
    highlight_color = "\033[33m\033[1m\033[4m"
    default_color = "\033[0m"

    print(f"{title} (running jobs are {highlight_color}highlighted{default_color}):")

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
    batch_cmd, logs = read_files(batch_path, base_name, log_path)
    finished_cmd, finished_ratio = check_progress(batch_cmd, logs)
    title = 'Experiment progress'
    batch_files = list(batch_cmd.keys())
    batch_info = {batch_file: f'{finished_ratio[batch_file][0]}/{finished_ratio[batch_file][1]}' for batch_file in
                  batch_files}
    show_batch_info(batch_files, batch_info, running_jobs, title)


def refresh_exps(batch_path, base_name, log_path, running_jobs=None):
    batch_cmd, logs = read_files(batch_path, base_name, log_path)
    finished_cmd, finished_ratio = check_progress(batch_cmd, logs)
    unfinished = get_unfinished(batch_cmd, finished_cmd)
    title = f"Write to {output_dir}"
    batch_files = list(batch_cmd.keys())
    batch_info = {}
    for filename in unfinished:
        lastname = os.path.basename(os.path.normpath(filename))
        w_name = os.path.join(output_dir, lastname)
        with open(w_name, 'w') as fd:
            fd.writelines(unfinished[filename])
        batch_info[filename] = f"wrote {len(unfinished[filename])} " \
                               f"remaining experiment" \
                               f"{'s' if len(unfinished[filename]) > 1 else ''}"
    show_batch_info(batch_files, batch_info, running_jobs, title)


def parse_common_args(args):
    batch_path = args.srcdir
    log_path = args.logdir
    base_name = args.base
    if args.range != 'all':
        base_name += args.range
    return batch_path, base_name, log_path


class JobBlock:
    def __init__(self, jobid, partition, name, *args, **kwargs):
        self.jobid = jobid
        self.partition = partition
        self.name = name

    def __str__(self):
        return f"JOB {self.jobid}: {self.partition}, {self.name}"

    def __repr__(self):
        return str(self)


def get_running_jobs():
    output = subprocess.check_output(
        ['squeue', '--format', '%.8i %.9P %100j', '--user', os.getenv('USER')],
    ).decode('utf-8')
    jobs = [JobBlock(*line.split(None)) for line in output.strip().split('\n')][1:]
    return jobs


def get_partition():
    output = subprocess.check_output(
        ['sinfo']
    ).decode('utf-8')
    regex = re.compile('[^\\w]')
    print(output)
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


def parse_run(args):
    batch_path, base_name, log_path = parse_common_args(args)
    jobs = get_running_jobs()
    partitions = get_partition()



parser = ArgumentParser()
subparsers = parser.add_subparsers()
parser_show = subparsers.add_parser('show', help='Show experiment progress.')
parser_gen = subparsers.add_parser('gen', help='Generate new experiment settings.')
parser_run = subparsers.add_parser('run', help='Run experiments.')
for parserx in [parser_show, parser_gen, parser_run]:
    parserx.add_argument('--base', default='autogen_sample_script_', help='Provide base name for autogen script.')
    parserx.add_argument('--range', choices=['node', 'graph', 'all'], default='all',
                         help='Select process range for autogen script.')
    parserx.add_argument('--srcdir', default=src_dir, help='Path to autogen script.')
    parserx.add_argument('--logdir', default=log_dir, help='Path to logs.')
parser_show.set_defaults(func=parse_show)
parser_gen.set_defaults(func=parse_gen)
parser_run.set_defaults(func=parse_run)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
