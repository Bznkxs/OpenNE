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
            ret += str(q).replace(',', ' ') + ", "
        ret += "\n"
    ret += "\n"
    return ret




class hlist(list):
    def get(self):
        return str(self[0:10])
    def __hash__(self):
        return hash(str(self[0:10]))

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

        for i in ['micro', 'macro', 'samples', 'weighted']:
            priority_list_args[1].append(i)
        tmp = 0
        rddd = {}
        for w in priority_list_args:
            for j in w:
                rddd[j] = tmp
                tmp += 1
        args['time'] = time
        nm = args['model']
        r_args = [(nm, hlist())]
        for i in priority_list_args[0]:
            r_args[0][1].append((i, args.get(i, '-')))
        for i in priority_list_args[1]:
            r_args[0][1].append((i, int(res[i]*10000+0.5)/10000))
        for i in priority_list_args[2]:
            r_args[0][1].append((i, args.get(i, '-')))
        return r_args, rddd



def main():
    os.system("git pull")
    curdir = os.path.abspath(__file__)[:-os.path.basename(__file__).__len__()]
    X = []
    print("????")
    for d in os.listdir(curdir):
        d = os.path.join(os.path.normpath(curdir), d)
        #print(d)
        if os.path.isfile(d) and d.endswith(".txt"):  # logfile
            try:
                x, rd = transfer(d)
                X.extend(x)

            except Exception as _:
                print(d)
                print(_)
                continue
    print(">")
    # sort
    # [("model", [("dataset", "cora"), (...)] )]
    print("# items:", len(X))

    X.sort(key=lambda x: (x[1][rd['dataset']][1],
                          x[1][rd['enc']][1],
                          x[1][rd['dec']][1],
                          x[1][rd['sampler']][1],
                          str(x[1][rd['lr']][1]),
                          str(x[1][rd['dim']][1]),
                          str(x[1][rd['hiddens']][1])
                          , -x[1][rd['micro']][1]))
    X = [X[i] for i in range(len(X)) if i == 0 or hash(X[i]) != hash(X[i-1])]
    print("# items:", len(X))

    x, y = 93,94
    print(X[x][1].get())
    print(X[y][1].get())
    print(X[x][1].__hash__())
    print(X[y][1].__hash__())
    print(X[x].__hash__())
    print(X[y].__hash__())
    sd = {X[x]: 1, X[y]: 2}
    print(sd[X[x]])
    print(sd[X[y]])
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
    #os.system("git add .")
    #os.system('git commit -m "update experiment data (automatic operation)"')
    #os.system("git push")

if __name__ == "__main__":
    main()


