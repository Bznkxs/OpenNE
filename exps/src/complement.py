import os
import re
from typing import Dict, List
from monitor import CMD

cur_dir = os.path.abspath(os.path.dirname(__file__))  # directory of this file
root_dir = os.path.normpath(os.path.join(cur_dir, '..', '..'))  # project root, directory of OpenNE
src_dir = os.path.join(root_dir, 'src')  # OpenNE/src
output_dir = os.path.normpath(os.path.join(src_dir, 'complement'))
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def complement():
    # find files with which we shall deal
    full_file_list = os.listdir(src_dir)
    real_file_list = []
    for filename in full_file_list:
        if filename.startswith('autogen_sample') and filename.endswith('.sh') and not filename[-4].isnumeric():
            # this is what we want
            real_file_list.append(filename)

    # read files
    lines: Dict[str, List[str]] = {}  # filename: [contents]
    for filename in real_file_list:
        full_path = os.path.join(src_dir, filename)
        with open(full_path, 'r') as f:
            lines[filename] = [i.strip() for i in list(f)]

    # automatic analysis
    newlines: Dict[str, List[str]] = {}
    for filename in real_file_list:

        cl = lines[filename]
        all_cmd = [CMD(cmd_str) for cmd_str in cl]
        all_cmd = [i for i in all_cmd if i.args]
        # first get all arg names
        print(all_cmd[0].__dict__)
        all_arg_names = list(all_cmd[0].argsdict.keys())

        # then determine which arg is changing
        changing_arg = None
        groups = []
        for i in range(len(all_cmd) - 1):
            flg = 0
            c_arg = None
            for arg in all_arg_names:
                if arg in all_cmd[i].argsdict and arg in all_cmd[i+1].argsdict and all_cmd[i].argsdict[arg] != all_cmd[i+1].argsdict[arg]:
                    flg += 1
                    c_arg = arg
            if flg == 1:
                changing_arg = c_arg
            else:
                groups.append(i)
        groups.append(len(all_cmd) - 1)

        # determine arg range
        arg_range = []
        pt = 0
        if changing_arg is not None:
            tmp_range = []
            for i in range(len(all_cmd) - 1):
                cmd = all_cmd[i]
                if cmd.argsdict[changing_arg] not in tmp_range:
                    tmp_range.append(cmd.argsdict[changing_arg])
                if i == groups[pt]:
                    if len(arg_range) < len(tmp_range):
                        arg_range = tmp_range
                    tmp_range = []
                    pt += 1

        print(filename, ": period =", len(arg_range))

        # fill absent ones
        newlines[filename] = []
        for i in groups:  # choose last one in group as repr
            cmd = all_cmd[i]
            for pt in range(len(arg_range)):
                # complete the lost experiments
                new_cmd = CMD(cmd.sorted_cmd_str)
                new_cmd.change_key(changing_arg, arg_range[pt])
                newlines[filename].append(new_cmd.sorted_cmd_str + '\n')

        with open(os.path.join(output_dir, filename), 'w') as f:
            f.writelines(newlines[filename])

if __name__ == '__main__':
    complement()
