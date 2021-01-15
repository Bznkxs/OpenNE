import os
import sys
import json


def dict_to_md_table(dict1):
    names, _ = zip(*dict1[0][1])

    # table header
    ret = "| name | "

    for i in names:
        ret += str(i) + " | "
    ret += "\n"
    ret += "|---|"
    for _ in names:
        ret += "---|"
    ret += "\n"
    # items
    for nm, ls in dict1:
        ret += "| " + str(nm) + " | "
        for p, q in ls:
            ret += str(q) + " | "
        ret += "\n"
    ret += "\n"
    return ret

def dict_to_csv(dict1):
    names, _ = zip(*dict1[0][1])

    # table header
    ret = "name, "

    for i in names:
        ret += str(i) + ", "
    ret += "\n"
    # items
    for nm, ls in dict1:
        ret += str(nm) + ", "
        for p, q in ls:
            ret += str(q) + ", "
        ret += "\n"
    ret += "\n"
    return ret

def transfer(filename):
    """
    transfer single log file into md
    @param filename: filename
    @return: two dicts
    """

    with open(filename, 'r') as f:
        # [("model", [("dataset", "cora"), (...)] )]
        args, res = f.__iter__()

        args = args[13:]  # "actual args: "
        args = args.replace("'",'"')
        args = args.replace("False", '"False"')
        args = args.replace("True", '"True"')

        res = res.replace("'",'"')
        # print(args)
        args = json.loads(args)
        res = json.loads(res)
        args.update(res)

        nm = os.path.basename(os.path.normpath(filename))
        nms = nm.split('_')
        time = nms[0][2:4] + '-' + nms[0][4:6] + '-' + nms[0][6:8] + ' ' + nms[1][:2] + ":" + nms[1][2:4] + ":" + nms[1][4:6]
        priority_list_args = [['dataset', 'enc', 'dec', 'sampler', 'epochs', 'lr','early_stopping', 'dim', 'hiddens', 'readout', 'est',  'time'],[], []]
        for i in res:
            priority_list_args[1].append(i)
        tmp = 0
        rddd = {}
        for w in priority_list_args:
            for j in w:
                rddd[j] = tmp
                tmp += 1
        args['time'] = time
        nm = args['model']
        r_args = [(nm, [])]
        for i in priority_list_args[0]:
            r_args[0][1].append((i, args.get(i, '-')))
        for i in res:
            r_args[0][1].append((i, int(res[i]*10000+0.5)/10000))
        for i in priority_list_args[2]:
            r_args[0][1].append((i, args.get(i, '-')))
        return r_args, rddd

if __name__ == "__main__":
    os.system("git pull")
    curdir = os.path.abspath(__file__)[:-os.path.basename(__file__).__len__()]
    X = []

    for d in os.listdir(curdir):
        d = os.path.join(os.path.normpath(curdir), d)
        print(d)
        if os.path.isfile(d) and d.endswith(".txt"):  # logfile
            try:
                x, rd = transfer(d)
                X.extend(x)

            except Exception as _:
                print(_)
                continue
    # sort
    # [("model", [("dataset", "cora"), (...)] )]
    X.sort(key=lambda x: (x[1][rd['enc']][1], -x[1][rd['micro']][1]))

    mdstr = "# Logs\n\n" + dict_to_md_table(X)
    mddir = os.path.join(curdir, "md")
    if not os.path.isdir(mddir):
        os.mkdir(mddir)
    with open(os.path.join(mddir, "logs.md"), 'w') as f:
        f.write(mdstr)

    csvstr = dict_to_csv(X)
    with open(os.path.join(mddir, "logs.csv"), 'w') as f:
        f.write(csvstr)

    os.chdir(curdir)
    os.system("git add .")
    os.system('git commit -m "update experiment data (automatic operation)"')
    os.system("git push")


