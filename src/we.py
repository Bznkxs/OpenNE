import os
import sys
import json


def dict_to_cmd(dict1):
    if len(dict1) == 0:
        return ""
    names, _ = zip(*dict1[0][1])

    # table header
    ret = ""
    # items
    for nm, ls in dict1:
        ret += "python3 -m openne "
        for p, q in ls:
            if q != "-":
                ret += "--" + p.replace('_', '-') + ' ' + str(q).replace('[', '').replace(']', '').replace(',', '') + " "
        ret += "$*\n"
    return ret


def transfer(filename):
    """
    transfer single log file into md
    @param filename: filename
    @return: two dicts
    """

    with open(filename, 'r', encoding='utf-8') as f:
        # [("model", [("dataset", "cora"), (...)] )]
        r_args = []
        tmp_args = []
        for line in f:
            if line.startswith("actual args:"):
                args = line
                args = args[13:]  # "actual args: "
                args = args.replace("'",'"')
                args = args.replace("False", '"False"')
                args = args.replace("True", '"True"')


                args = json.loads(args)

                priority_list_args = [['model', 'dataset', 'enc', 'dec', 'sampler', 'epochs', 'lr','early_stopping', 'dim', 'hiddens', 'readout', 'est']]

                nm = args['model']
                tmp_args = [(nm, [])]
                for i in priority_list_args[0]:
                    tmp_args[-1][1].append((i, args.get(i, '-')))
                r_args.extend(tmp_args)
            elif line.startswith("{micro:"):
                r_args.pop(-1)
        return r_args

def main():
    curdir = os.path.abspath(__file__)[:-os.path.basename(__file__).__len__()]
    X = []

    for d in os.listdir(curdir):
        d = os.path.join(os.path.normpath(curdir), d)
        print(d)
        if os.path.isfile(d) and d.endswith(".out"):  # logfile
            x = transfer(d)
            cmdstr = dict_to_cmd(x)
            wr = os.path.join(curdir, "fix_" + os.path.basename(d.replace('.out', '.sh')))
            print(wr)
            with open(wr, 'w') as f:
                f.write(cmdstr)



if __name__ == "__main__":
    main()


