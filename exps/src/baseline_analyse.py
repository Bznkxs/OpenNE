import json
import os
import random

import pandas
import seaborn as sns
import matplotlib.pyplot as plt
from monitor import CMD, processed_dir, src_dir, get_CMD
from new_samplefullexps import gethyper, hyperparameter_list

csv_name = 'failure_analysis.csv'
output_name = 'best_model_analysis.csv'
full_csv_path = os.path.join(processed_dir, csv_name)
full_output_path = os.path.join(processed_dir, output_name)
output_latex_name = 'best_model_analysis.tex'
full_output_latex_path = os.path.join(processed_dir, output_latex_name)

settings_path = os.path.join(processed_dir, '..', 'settings.json')
fig_path = os.path.join(processed_dir, "..", "graph")

modelargs = ['enc', 'sampler', 'dec', 'est', 'readout']
baselines = {"gae": {
                "enc": "gcn",
                "sampler": "node-neighbor-random",
                "dec": "inner",
                "est": "jsd",
                "readout": "mean"
            },
            "dgi": {
                "enc": "gcn",
                "sampler": "dgi",
                "dec": "bilinear",
                "est": "jsd",
                "readout": "mean"
            },
            "mvgrl": {
                "enc": "gcn",
                "sampler": "mvgrl",
                "dec": "inner",
                "est": "jsd",
                "readout": "sum"
            },
            "gca": {
                "enc": "gcn",
                "sampler": "gca",
                "dec": "inner",
                "est": "nce",
                "readout": "mean"
            },
            "infograph": {
                "enc": "gin",
                "sampler": "dgi",
                "dec": "inner",
                "est": "jsd",
                "readout": "sum"
            },
            "graphcl": {
                "enc": "gin",
                "sampler": "aug",
                "dec": "inner",
                "est": "nce",
                "readout": "sum"
            }
}


def getmodel(argsdict):
    ma_list = []
    for ma_key in modelargs:
        ma_list.append(argsdict.get(ma_key, None))
    return tuple(ma_list)


baseline_dict = {getmodel(modelargsdict): modelname for modelname, modelargsdict in baselines.items()}
# print(baseline_dict)

def get_baseline(cmd: CMD):
    model_tuple = getmodel(cmd.argsdict)
    if model_tuple in baseline_dict:
        return baseline_dict[model_tuple]
    return "others"

def normalize(x):
    n_set = {
        'GIN', 'GCN', 'GAT', 'DGI', 'MVGRL',
        'Bilinear', 'Inner',
        'NCE', 'JSD',
        'Mean', 'Sum',
        'InfoGraph',
        'JK-Net',
        'GAE',
        'GCA',
        'GraphCL',
        'MUTAG',
        'Cora',
        'CiteSeer',
        'PubMed',
        'IMDB MULTI',
        'IMDB BINARY',
        'Amazon Computers',
        'Amazon Photo',
        'Reddit BINARY',
        'PTC_MR',
        'WikiCS',
        'Coauthor CS',
        'Coauthor Phy'
    }
    if isinstance(x, str):
        x = x.replace('node-neighbor-random', 'LINE')\
        .replace('node-rand_walk-random', 'DeepWalk')\
        .replace('aug', 'GraphCL').replace("'", '')
        for w in n_set:
            if w.lower().replace('_', ' ') == x.strip().lower().replace('_', ' '):
                return w
    return x

def get_model_name(cmd: CMD):
    model_tuple = getmodel(cmd.argsdict)
    if model_tuple in baseline_dict:
        return normalize(baseline_dict[model_tuple])
    model_tuple = tuple(normalize(x) for x in model_tuple)

    return f'"{str(model_tuple)}"'.replace('node-neighbor-random', 'LINE')\
        .replace('node-rand_walk-random', 'DeepWalk')\
        .replace('aug', 'GraphCL').replace("'", '')
    # for modelname in baselines:
    #     model = baselines[modelname]
    #     flg = True
    #     for key in model:
    #         if cmd.argsdict[key] != model[key]:
    #             flg = False
    #             break
    #     if flg:
    #         return modelname
    # return 'others'

    
def analyse():
    # step 1. open csv
    table = pandas.read_csv(full_csv_path)
    finished = table[table['status'] == 'finished']
    finished['basemodel'] = finished['raw_cmd'].map(lambda x: get_baseline(CMD(x)))
    results = {}
    all_max = {}  # {dataset: (res, cmd)}
    for i, exp in finished.iterrows():
        cmd = CMD(exp['raw_cmd'])
        res = float(exp['result'])
        results[cmd.sorted_cmd_str] = res
        dataset = cmd.argsdict['dataset']
        flg = 0
        for kw in ['except_neighbor', 'jk-net', 'mlp']:
            if cmd.sorted_cmd_str.find(kw) >= 0:
                flg = 1
                break
        if flg == 1:
            continue
        if dataset not in all_max:
            all_max[dataset] = (res, cmd)
        elif all_max[dataset][0] < res:
            all_max[dataset] = (res, cmd)

    # remove unwanted exps

    basetable = finished[finished['basemodel'] != 'others']



    print(basetable['basemodel'].value_counts())
    print(list(results)[:10])

    # step 2. open baselines
    dirlist = os.listdir(src_dir)
    # step 2.1. find baseline files
    script_prefix = 'autogen_script_baselines_'
    script_suffix = '.sh'
    baseline_files = [os.path.join(src_dir, x) for x in dirlist if x.startswith(script_prefix) and x.endswith(script_suffix)]
    # step 2.2. read cmd
    cmd_dict = get_CMD(baseline_files)
    print(len(cmd_dict))

    # step 3. analyse
    exp_res_dict = {}

    with open(full_output_path, 'w') as fo:
        # print('dataset,model,max,raw_cmd', file=fo)
        print('Task,Dataset,"Best design \nin design space","Best \nscore","Best \nbaseline","Best score \nof baseline"', file=fo)
        for batch_name in cmd_dict:
            res_frame = pandas.DataFrame()
            exps = []
            models = []
            datasets = []
            hypers = []
            res = []
            dataset = (cmd_dict[batch_name][0]).argsdict['dataset']
            task = (cmd_dict[batch_name][0]).argsdict['task']
            if task.find('graph') != -1:
                task = 'graph'
            else:
                task = 'node'
            print(dataset, ': len =', len(cmd_dict[batch_name]))
            # we can directly use data in table
            #sns.boxplot(x='')

            # step 3.1. walk through to get basic stats
            exp_res_dict[dataset] = {}
            for cmd in cmd_dict[batch_name]:

                if cmd.sorted_cmd_str not in results:
                    continue

                model = get_baseline(cmd)
                hyper = gethyper(cmd)
                if model not in exp_res_dict[dataset]:
                    exp_res_dict[dataset][model] = {'stats': {}, 'data': {}}

                exp_res_dict[dataset][model]['data'][cmd.sorted_cmd_str] = results[cmd.sorted_cmd_str]
                exps.append(cmd.sorted_cmd_str)
                models.append(model)
                datasets.append(dataset)
                hypers.append(hyper)
                res.append(results[cmd.sorted_cmd_str])
            res_frame['exp'] = exps
            res_frame['model'] = models
            res_frame['dataset'] = datasets
            res_frame['hyper'] = hypers
            res_frame['res'] = res

            # step 3.2. model-wise max, mean, etc.
            best_baseline = None
            best_baseline_score = 0
            for model in exp_res_dict[dataset]:
                mxm = 0
                mxi = None
                sum_res = 0
                len_res = len(exp_res_dict[dataset][model]['data'])
                for cmdstr, res in exp_res_dict[dataset][model]['data'].items():
                    if mxm < res:
                        mxm = res
                        mxi = cmdstr
                    sum_res += res
                exp_res_dict[dataset][model]['stats'] = {
                    'max': mxm,
                    'mxi': mxi,
                    'len': len_res,
                    'sum': sum_res,
                    'mean': sum_res / len_res
                }

                print(dataset, ',', model, ':', len_res, mxm, sum_res / len_res)
                if best_baseline_score < mxm:
                    best_baseline_score = mxm
                    best_baseline = CMD(mxi)

            print(
                task,
                normalize(dataset),
                get_model_name(all_max[dataset][1]),
                all_max[dataset][0],
                get_model_name(best_baseline),
                best_baseline_score,
                sep=',',
                file=fo
            )
                # print(dataset, model, mxm, mxi, sep=',', file=fo)
            # print(dataset, get_baseline(all_max[dataset][1]), all_max[dataset][0], all_max[dataset][1], sep=',', file=fo)
            print(task, ',', normalize(dataset), ',', get_baseline(all_max[dataset][1]), ':', '?', all_max[dataset][0], all_max[dataset][1])

            # # step 3.3. paint
            # plt.figure()
            # sns.boxplot(x='model', y='res', data=res_frame)
            # sns.swarmplot(x='model', y='res', data=res_frame, color=".25")
            # plt.savefig(os.path.join(fig_path, f'baseline_{dataset}.png'))
    # indices = pandas.MultiIndex(('task', 'dataset'))
    output_df = pandas.read_csv(full_output_path, index_col=(1,))
    print(output_df)
    output_df = output_df.sort_values('Task')
    output_df = output_df.drop(columns=['Task'])
    print(output_df)

    output_df.to_latex(full_output_latex_path)


if __name__ == '__main__':
    analyse()