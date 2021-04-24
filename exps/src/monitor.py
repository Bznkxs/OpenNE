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
        self.start = self.args[0]
        self.args = self.args[1:]
        self.args.sort()
        self.args = [self.start] + self.args
        self.sorted_cmd_str = '--'.join(self.args)

    def __str__(self):
        return self.sorted_cmd_str

    def __repr__(self):
        return self.sorted_cmd_str

    def __hash__(self):
        return hash(self.sorted_cmd_str)


def normalcmd(cmd):
    return CMD(cmd).sorted_cmd_str


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


def search_batch_files(path, base_name, leaf=True):
    """
    Two modes: if leaf==True, keeps only the 'leaf files' in `path` with prefix `base_name` and suffix '.sh'
    e.g. if we have enc.sh, enc_0.sh, enc_1.sh, this will return the latter two files
    if leaf==False, keeps only the 'root files'.
    @param path:
    @param base_name: a list of base names
    @param leaf: mode selection
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
            if leaf:
                prefix = prefix_of(batch_files, fd)
                if prefix is not None:
                    remove(prefix)
                child = has_prefix(batch_files, fd)
                if child is None:
                    add(fd)
            else:
                child = has_prefix(batch_files, fd)
                while child is not None:
                    remove(child)
                    child = has_prefix(batch_files, fd)
                prefix = prefix_of(batch_files, fd)
                if prefix is None:
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

    # display
    title = 'Experiment progress'
    batch_files = list(batch_cmd.keys())
    batch_info = {batch_file: f'{finished_ratio[batch_file][0]}'
                              f'/{finished_ratio[batch_file][1]}'
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


def refresh_exps(batch_path, base_name, log_path, running_jobs=None, display=True):
    batch_cmd, logs = read_files(batch_path, base_name, log_path)
    finished_cmd, finished_ratio = check_progress(batch_cmd, logs)
    unfinished = get_unfinished(batch_cmd, finished_cmd)
    ret = write_exps(unfinished)

    # display
    if display:
        title = f"Write to {output_dir}"
        batch_files = list(batch_cmd.keys())
        batch_info = {filename: f"wrote {len(unfinished[filename])} "
                                f"remaining experiment"
                                f"{'s' if len(unfinished[filename]) > 1 else ''}"
                                f" out of {len(batch_cmd[filename])} total"
                      for filename in unfinished}
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


def run_job_sbatch(name, partition):
    modify_batch = False
    with open(name, 'r') as fd:
        lines = list(fd)
        if len(lines) == 0 or not lines[0].startswith('#!'):
            modify_batch = True

    if modify_batch:
        with open(name, 'w') as fd:
            fd.write("#!/bin/sh\n")
            fd.write('\n'.join(lines))
    tmpdir = os.curdir
    os.chdir(src_dir)
    print(f"run {name} with partition {partition}")
    subprocess.run(['sbatch', '-G', '1', '-p', partition, name])
    os.chdir(tmpdir)
    # subprocess.run(['sbatch', '-G', '1', '-p', partition, name])


def stop_job_sbatch(name, jobid):
    print(f"stop {name} (jobid: {jobid})")
    subprocess.run(['scancel', jobid])


def run_batch_files(batch_file_names, partitions):
    for name in batch_file_names:
        run_job_sbatch(name, partitions[0])


def stop_batch_files(batch_file_names, jobs):
    for name in batch_file_names:
        if os.path.basename(name) in jobs:
            stop_job_sbatch(name, jobs[os.path.basename(name)].jobid)



def parse_run(args):
    batch_path, base_name, log_path = parse_common_args(args)
    jobs = get_running_jobs()
    partitions = get_partition()
    if len(partitions) == 0:
        print("No partitions available!")
        exit(1)

    #  update experiment
    batch_file_names = refresh_exps(batch_path, base_name, log_path, jobs)

    #  do not update
    # batch_file_names = search_batch_files(batch_path, base_name)
    # for name in batch_file_names:
    #     if os.path.basename(name) not in jobs:
    #         run_job_sbatch(name, partitions[0])

    stop_batch_files(batch_file_names, jobs)
    run_batch_files(batch_file_names, partitions)



def parse_stop(args):
    batch_path, base_name, log_path = parse_common_args(args)
    jobs = get_running_jobs()

    batch_file_names = search_batch_files(batch_path, base_name)
    stop_batch_files(batch_file_names, jobs)




parser = ArgumentParser()
subparsers = parser.add_subparsers()
parser_show = subparsers.add_parser('show', help='Show experiment progress.')
parser_gen = subparsers.add_parser('gen', help='Generate new experiment settings.')
parser_run = subparsers.add_parser('run', help='Run experiments.')
parser_stop = subparsers.add_parser('stop', help='Stop experiments.')

for parserx in [parser_show, parser_gen, parser_run, parser_stop]:
    parserx.add_argument('--base', default='autogen_sample_script_', help='Provide base name for autogen script.')
    parserx.add_argument('--range', nargs='*', default=[''],
                         help='Select process range for autogen script.')
    parserx.add_argument('--srcdir', default=src_dir, help='Path to autogen script.')
    parserx.add_argument('--logdir', default=log_dir, help='Path to logs.')

parser_show.set_defaults(func=parse_show)
parser_gen.set_defaults(func=parse_gen)
parser_run.set_defaults(func=parse_run)
parser_stop.set_defaults(func=parse_stop)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
