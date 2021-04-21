import pandas as pd
import seaborn as sns
import sys
import os
import time
from sys import argv

curdir = os.path.dirname(__file__)
sys.path.extend([os.path.join(curdir, '')])

exp_name = 'graph_readout'
script_name = os.path.join(curdir, '../../src/autogen_sample_script_' + exp_name + '.sh')
xls_name = os.path.join(curdir, '../processed/exp_data_for_human.xls')
csv_name = os.path.join(os.path.dirname(__file__), '../processed/logs.csv')

# set style
sns.set(style='whitegrid')

try:
    from . import parse_exps
    from . import logs_to_md
    from logs_to_md import update
    from parse_exps import ExpVariable
except Exception as _:
    import parse_exps
    import logs_to_md
    from logs_to_md import update
    from parse_exps import ExpVariable
import numpy as np


def gen_work_table(exps: ExpVariable, exp_run, exp_name):
    datasets = list(exps.vars['dataset'].select('unigraph')) + list(exps.vars['dataset'].select('multigraph'))
    table = [[]]
    table[0] = ['', '', '', '', '', ''] + datasets
    attrs = ['enc', 'dec', 'sampler', 'readout', 'est']
    hyperattrs = ['epochs', 'early-stopping', 'lr', 'dim', 'hiddens']
    hyperattrs1 = ['epochs', 'early_stopping', 'lr', 'dim', 'hiddens']
    modelset = {}

    def parse_exp(exp):
        model = exp['_model']
        dataset = exp['dataset']
        hyper = exp['_hyperparameters']
        if hyper['_hiddens'] == 0:
            hyper['hiddens'] = '-'
        else:
            hyper['hiddens'] = '[' + '  '.join([hyper['dim']] * hyper['_hiddens']) + ']'
        modelstr = ','.join([optname] + [model[attr] for attr in attrs])
        hyperstr = ','.join([hyper[hyp] for hyp in hyperattrs])
        hyper.pop('hiddens')
        return model, dataset, hyper, modelstr, hyperstr

    # run 1 -- framework of exp. table, get menu of experiment plan
    split_exp = exps.split[exp_name]
    exp_plan = {parse_exps.gen_bash(k): {"done": False, "priority": 0} for k in split_exp}
    #print(exp_plan)
    for optname, i in exps.opt_groups.items():
        print("optname", optname)
        if optname[-1].isdigit():
       #     print(" digit", optname[-1])
            for k in exps.opt_groups[optname]:
                kstr = parse_exps.gen_bash(k)
                if kstr in exp_plan.keys():
                    exp_plan[kstr]["priority"] = int(optname[-1])
       #         if optname[-1] == "1":
       #             print(parse_exps.gen_bash(k))
            continue

        for exp in i:
            model, dataset, hyper, modelstr, hyperstr = parse_exp(exp)
            if modelstr in modelset:
                if dataset in modelset[modelstr]:
                    modelset[modelstr][dataset][hyperstr] = 1
                else:
                    modelset[modelstr][dataset] = {hyperstr: 1}

            else:
                modelset[modelstr] = {dataset: {hyperstr: 1}}

    # get exp opt group
    opt_groups = {"node_node": "ss_nodemodel",
                  "node_graph": "ss_gae",
                  "graph_node": "ss_graphmodel",
                  "graph_graph": "ss_gaeg"}
    opt_groups_lookup = {v: k for (k, v) in opt_groups.items()}
   # print(modelset.keys())
   # print("---")

    # run 2 -- look through log files and mark
    for exp in exp_run.iterrows():
        exp = exp[1]
        flg = 0
        try:
            dataset = exp['dataset']
            flg = 1
            model = [exp[attr] for attr in attrs]
            flg = 2
            optname = opt_groups_lookup[exp['name']]
            flg = 3
            hyper = [str(exp[hyperattr]) for hyperattr in hyperattrs1]
        except KeyError as _:
            print(_)
            continue
        modelstr = ','.join([optname] + model)
        hyperstr = ','.join(hyper)
        # print(modelstr, dataset, hyperstr)
        if modelstr in modelset:
            if dataset in modelset[modelstr]:
                if hyperstr in modelset[modelstr][dataset]:
                    modelset[modelstr][dataset][hyperstr] = 3
                  #  print("#3")
                    # print(modelstr, dataset, hyperstr)
                else:
                  #  print("#2")
                    pass
                    # print(222, hyperstr, ":", modelstr, dataset, modelset[modelstr][dataset].keys())
            else:
               # print("#1")
                pass
                # print(111)
        else:
           # print("#0")
            pass
            # print(1000, modelstr)

    # run 3 -- go through exp plan again and finish table
    for optname, i in exps.opt_groups.items():
        if optname[-1].isdigit():
            continue
        for exp in i:
            model, dataset, hyper, modelstr, hyperstr = parse_exp(exp)
            if modelset[modelstr][dataset][hyperstr] == 3:
                kstr = parse_exps.gen_bash(exp)
                if kstr in exp_plan.keys():
                    exp_plan[kstr]['done'] = True

    l1 = [(k, v) for k, v in modelset.items()]
    l1.sort(key=lambda x: x[0])
    for (k, v) in l1:  # k: name of model str; v: {all datasets: apperance}
        item = k.split(',')
        for ds in datasets:
            if ds in v:
                a, b = 0, 0
                for hypers in v[ds]:
                    if v[ds][hypers] == 3:
                        a += 1
                    b += 1
                item.append(str(a) + '/' + str(b))
            else:
                item.append('')
        table.append(item)
    table = np.array(table, dtype='str')

    return table, exp_plan


def draw_table(table):
    import xlwt

    colors = ['orange', 'light_orange',
              'light_yellow', 'ivory',
              'pale_blue', 'ice_blue',
              'coral', 'light_orange',
              'lime', 'light_green',
              'lavender', 'rose']
    style = [xlwt.easyxf(f'pattern: pattern solid, fore_colour {color}') for color in colors]

    # colors_data = [2, 53, 51, 34, 43, 26, 42, 55, 50, 3]
    colors_data = [2, 51, 26, 42, 50, 3]
    colorscale = len(colors_data)
    patterns = [xlwt.Pattern() for _ in range(colorscale)]
    for i in range(colorscale):
        patterns[i].pattern = xlwt.Pattern.SOLID_PATTERN
        patterns[i].pattern_fore_colour = colors_data[i]
    styles_data = [xlwt.XFStyle() for _ in range(colorscale)]
    for i in range(colorscale):
        styles_data[i].pattern = patterns[i]
    style_invalid = xlwt.easyxf(f'pattern: pattern solid, fore_colour gray25')
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('data', cell_overwrite_ok=True)
    booksheet.col(3).width = 256 * 30
    colcolors = [0] * 6
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            if i > 0 and j < 6:
                if table[i, j] != table[i - 1, j]:
                    colcolors[j] += 1
                coloridx = colcolors[j] % 2 + j * 2
                booksheet.write(i, j, table[i, j], style[coloridx])
            elif i == 0:
                if 5 < j < 9:
                    coloridx = 6
                    booksheet.write(i, j, table[i, j], style[coloridx])
                elif j > 8:
                    coloridx = 7
                    booksheet.write(i, j, table[i, j], style[coloridx])

            else:
                if table[i, j] != '':
                    a, b = table[i, j].split('/')
                    ratio = int(a) * (colorscale - 1) // int(b)
                    # print(a, b, ratio)
                    booksheet.write(i, j, table[i, j], styles_data[ratio])
                else:
                    booksheet.write(i, j, '', style_invalid)
    for j in range(colorscale):
        booksheet.write(table.shape[0] + 1, j, '', styles_data[j])
    workbook.save(xls_name)


def generate_exp_data():
    data = pd.read_csv(csv_name, skipinitialspace=True)

    # get datasets
    # datasets = set(data['dataset'])
    # for dataset in datasets:
    #     subdata = data[data['dataset'] == dataset]

    # all experiment settings are stored in OpenNE/exps/settings.json
    exps = parse_exps.parse()

    # generate work-table
    table, exp_plan = gen_work_table(exps, data, exp_name)

    # draw table
    try:
        draw_table(table)
    except Exception as _:
        print(_)
        print("will not generate table for human")

    # generate command series
    # print("done\n", '\n '.join([f'{k} ****** {v}' for (k, v) in exp_plan.items() if v['done']]))
    if len(argv) == 3 and argv[2] == 'minimal':
        exp_plan = [(k, v) for (k, v) in exp_plan.items() if v['priority'] == 1]
    else:
        exp_plan = [(k, v) for (k, v) in exp_plan.items()]
    all_exps = len(exp_plan)
    #print(all_exps, list(exp_plan.keys())[0], list(exp_plan.items())[0])
    #print(all_exps, exp_plan[:10])
    exp_plan = [(k, v) for (k, v) in exp_plan if not v['done']]
    new_exps = len(exp_plan)
    print(f"Experiment progress = {all_exps-new_exps}/{all_exps}")
    if argv[1] == 'gen':
        exp_plan.sort(key=lambda x: -x[1]['priority'])
        with open(script_name, 'w') as fp:
            for (k, v) in exp_plan:
                print(k, file=fp)

    # print(data)
    # sns.violinplot(x='enc', y='micro', hue='dataset', data=data)
    # plt.show()


if __name__ == '__main__':
    """
    args: 
    [0] process.py
    [1] gen/show
        - gen = generate new experiment commands
        - show = show progress
    [2] (optional) <GROUP_NAME>
        - minimal = minimal experiment group
        * default: full
    """
    assert argv[1] in ['gen', 'show']
    if argv[1] == 'show':
        while 1:
            update()
            generate_exp_data()
            time.sleep(20)
    else:
        update()
        generate_exp_data()
