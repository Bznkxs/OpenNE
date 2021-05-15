import copy
import os
import random
from typing import Dict, List, Tuple

from monitor import CMD, src_dir

hyperparameter_list = ['dim', 'hiddens', 'lr']

def readall():
    # step 0. read files
    fullexps_name = os.path.join(src_dir, 'autogen_script_baselines.sh')
    with open(fullexps_name, 'r') as f:
        lines = [CMD(line.strip()) for line in list(f)]
        lines = [x for x in lines if x.args is not None]
    return lines

def gethyper(cmd: CMD):
    hp_list = []
    for hp_key in hyperparameter_list:
        hp_list.append(cmd.argsdict.get(hp_key, None))
    return tuple(hp_list)

def sample(lines: List[CMD]):
    # step 1. collect CMDs with same datasets
    dataset_cmd_dict: Dict[str, List[CMD]] = {}
    for line in lines:
        dataset = line.argsdict['dataset'].strip()
        if dataset not in dataset_cmd_dict:
            dataset_cmd_dict[dataset] = []
        dataset_cmd_dict[dataset].append(line)


    # step 2. random sample hyperparameters w.r.t. datasets (brute force)
    hyperparameters: Dict[str, List[Tuple]] = {}
    hyperrank: Dict[str, Dict[Tuple, int]] = {}
    for dataset in dataset_cmd_dict:
        hyperparameters_ = set()
        for cmd in dataset_cmd_dict[dataset]:
            hyperparameters_.add(gethyper(cmd))
        hyperparameters_ = list(hyperparameters_)
        random.shuffle(hyperparameters_)

        hyperparameters[dataset] = hyperparameters_
        hyperrank[dataset] = {k: v for v, k in enumerate(hyperparameters_)}


    # step 3. select new exps
    new_exps: Dict[str, List[CMD]] = {}
    for dataset in dataset_cmd_dict:
        cmds = copy.deepcopy(dataset_cmd_dict[dataset])
        cmds.sort(key=lambda x: (hyperrank[dataset][gethyper(x)], str(x)))
        new_exps[dataset] = cmds


    # step 4. real sample
    sampled_new_exps: Dict[str, List[CMD]] = {}
    other_exps = {}
    for dataset in dataset_cmd_dict:
        sampled_new_exps[dataset] = [x for x in new_exps[dataset] if hyperrank[dataset][gethyper(x)] < 5]
        other_exps[dataset] = [x for x in new_exps[dataset] if hyperrank[dataset][gethyper(x)] >= 5]

    # step 5. write file
    all_sampled_output = os.path.join(src_dir, f'autogen_sample_script_baselines_0base5.sh')
    all_other_output = os.path.join(src_dir, f'autogen_sample_script_baselines_1more.sh')
    with open(all_sampled_output, 'w') as fa:
        with open(all_other_output, 'w') as fao:
            for dataset in dataset_cmd_dict:
                # sampled first
                sampled_output = os.path.join(src_dir, f'autogen_sample_script_baselines_0base5_{dataset}.sh')
                with open(sampled_output, 'w') as f:
                    for x in sampled_new_exps[dataset]:
                        print(str(x), file=f)
                        print(str(x), file=fa)
                other_output = os.path.join(src_dir, f'autogen_sample_script_baselines_1more_{dataset}.sh')
                with open(other_output, 'w') as f:
                    for x in other_exps[dataset]:
                        print(str(x), file=f)
                        print(str(x), file=fao)
                # full next
                full_output = os.path.join(src_dir, f'autogen_script_baselines_{dataset}.sh')
                with open(full_output, 'w') as f:
                    for x in new_exps[dataset]:
                        print(str(x), file=f)

    # fin

if __name__ == '__main__':
    lines = readall()
    sample(lines)