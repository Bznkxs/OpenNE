import os
import sys
import json
import tqdm

curdir = os.path.dirname(__file__)

menu_name = os.path.join(curdir, "../processed/menu.json")
md_name = os.path.join(curdir, "../processed/(deprecated)logs.md")
csv_name = os.path.join(curdir, "../processed/logs.csv")

def dict_to_md_table(dict1, deprecated=False):
    if deprecated:
        return '', ''
    if len(dict1) == 0:
        return '', ''
    header = "# Logs\n\n"
    names, _ = zip(*dict1[0][1])

    # table header
    header += "| name | "

    for i in names:
        header += str(i) + " | "
    header += "\n"
    header += "|---|"
    for _ in names:
        header += "---|"
    header += "\n"
    body = ''
    # items
    for nm, ls in dict1:
        body += "| " + str(nm) + " | "
        for p, q in ls:
            body += str(q) + " | "
        body += "\n"
    body += "\n"
    return header, body


def dict_to_csv(dict1, header=True):
    if len(dict1) == 0:
        return ''
    names, _ = zip(*dict1[0][1])
    ret = ''
    if header:
        # table header
        ret += "name, "

        for i in names:
            ret += str(i) + ", "
        ret += "\n"
    # items
    for nm, ls in dict1:
        ret += str(nm) + ", "
        for p, q in ls:
            ret += str(q).replace(',', ' ') + ", "
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
    try:
        with open(filename, 'r') as f:
            # [("model", [("dataset", "cora"), (...)] )]
            log_output = list(f.__iter__())
            args, res = log_output[-2:]

            args = args[13:]  # "actual args: "
            args = args.replace("'", '"')
            args = args.replace("False", '"False"')
            args = args.replace("True", '"True"')

            res = res.replace("'", '"')
            # print(args)
            args = json.loads(args)
            res = json.loads(res)
            args.update(res)

            nm = os.path.basename(os.path.normpath(filename))
            nms = nm.split('_')
            time = nms[0][2:4] + '-' + nms[0][4:6] + '-' + nms[0][6:8] + ' ' + nms[1][:2] + ":" + nms[1][2:4] + ":" + nms[
                                                                                                                          1][
                                                                                                                      4:6]
            priority_list_args = [
                ['dataset', 'enc', 'dec', 'sampler', 'epochs', 'lr', 'early_stopping', 'dim', 'hiddens', 'readout', 'est',
                 'time'], [], []]
            default_value = {
                'dataset': '-',
                'enc': '-',
                'dec': '-',
                'sampler': '-',
                'epochs': '500',
                'lr': '0.01',
                'early_stopping': '20',
                'dim': '128',
                'hiddens': '-',
                'readout': 'mean',
                'est': 'jsd',
                'time': '-',
                'micro': '-',
                'macro': '-',
                'samples': '-',
                'weighted': '-'
            }
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
                r_args[0][1].append((i, args.get(i, default_value[i])))
            for i in priority_list_args[1]:
                r_args[0][1].append((i, int(res[i] * 10000 + 0.5) / 10000))
            for i in priority_list_args[2]:
                r_args[0][1].append((i, args.get(i, default_value[i])))
            return r_args, rddd
    except Exception as _:
        print("cannot open file?", _)

def update(clear=False, md_deprecated=True):
    flag = 0
    try:
        assert not clear
        with open('../processed/menu.json', 'r') as fp:
            menu = json.load(fp)
            flag = 1
    except Exception as _:
        menu = []
        flag = 0
    menu = set(menu)
    curdir = os.path.abspath(__file__)[:-os.path.basename(__file__).__len__()]
    logdir = os.path.normpath(os.path.join(curdir, '..', '..', 'src', 'logs'))
    print("reading files from", logdir)
    X = []
    ld = os.listdir(logdir)
    for i, d in tqdm.tqdm(enumerate(ld), total=len(ld)):
        _d = d
        d = os.path.join(os.path.normpath(logdir), d)
        # print(d)
        if os.path.isfile(d) and d.endswith(".txt"):  # logfile
            if _d in menu:
                continue
            try:
                x, rd = transfer(d)
                X.extend(x)
                menu.add(_d)
            except Exception as _:
                print("file", d)
                print(_)
                continue
    with open(menu_name, 'w') as fp:
        json.dump(list(menu), fp)

    print(">")
    # sort
    # [("model", [("dataset", "cora"), (...)] )]
    print("# items:", len(X))

    X.sort(key=lambda x: (x[1][rd['dataset']][1],
                          x[1][rd['enc']][1],
                          x[1][rd['dec']][1],
                          x[1][rd['sampler']][1],
                          x[1][rd['readout']][1],
                          x[1][rd['est']][1],
                          str(x[1][rd['lr']][1]),
                          str(x[1][rd['dim']][1]),
                          str(x[1][rd['hiddens']][1])
                          , -x[1][rd['micro']][1]))
    # X = [X[i] for i in range(len(X)) if i == 0 or hash(X[i]) != hash(X[i - 1])]
    X = []
    print("# items:", len(X))

    mdstr_header, mdstr_body = dict_to_md_table(X, md_deprecated)
    mddir = os.path.join(curdir, "")
    if not os.path.isdir(mddir):
        os.mkdir(mddir)
    if flag == 0:
        csvstr = dict_to_csv(X)
        mdstr = mdstr_header + mdstr_body
        open_mode = 'w'
    else:
        csvstr = dict_to_csv(X, False)
        mdstr = mdstr_body
        open_mode = 'a'
    if not md_deprecated:
        with open(os.path.join(mddir, md_name), open_mode) as f:
            f.write(mdstr)

    with open(os.path.join(mddir, csv_name), open_mode) as f:
        f.write(csvstr)

    os.chdir(curdir)

from sys import argv
if __name__ == "__main__":
    if len(argv) == 2 and argv[1] == 'clear':
        update(True)
    else:
        update(False)
