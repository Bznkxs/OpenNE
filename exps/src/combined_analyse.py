import json
import os
import random
from multiprocessing import Pool
from typing import Iterable

import numpy as np

import pandas
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm

import parse_exps
from parse_exps import cartesian_prod
from monitor import CMD, processed_dir, src_dir, get_CMD, get_cmd
from new_samplefullexps import gethyper, hyperparameter_list
from baseline_analyse import getmodel, modelargs

csv_name = 'failure_analysis.csv'
output_name = 'combined_model_analysis.csv'
full_csv_path = os.path.join(processed_dir, csv_name)
full_output_path = os.path.join(processed_dir, output_name)

settings_path = os.path.join(processed_dir, '..', 'settings.json')
fig_path = os.path.join(processed_dir, "..", "graph")

datasets = ['cora', 'citeseer', 'pubmed', 'coauthor_cs', 'coauthor_phy',
            'wikics', 'amazon_photo', 'amazon_computer', 'mutag', 'imdb_binary',
            'imdb_multi', 'reddit_binary', 'ptc_mr']

if not os.path.exists(fig_path):
    os.makedirs(fig_path)


def create_table(cmd_list, results, smooth=False):
    args = 'dataset,enc,dec,sampler,readout,est,dim,hiddens,raw,res'.split(',')
    if smooth:
        results = results.copy()
        for cmd in cmd_list:
            if str(cmd) not in results:
                results[str(cmd)] = -1
    def default(arg, c):
        if arg == 'raw':
            return str(c)
        if arg == 'res':
            return results[str(c)]
        return None

    wdict = {a: [] for a in args}
    for cmd in cmd_list:
        if str(cmd) in results:
            for i in args:
                wdict[i].append(cmd.argsdict.get(i, default(i, cmd)))


    table = pandas.DataFrame()
    for a in args:
        table[a] = wdict[a]

    return table


def entropy(it):
    return scipy.stats.entropy(it)
    # res = 0
    # ans = 1
    # for x in it:

def work(args):
    table, thresholds, n_all, n_1 = args
    for threshold in thresholds:
        quantiles = table.groupby('dataset')['res'].quantile(threshold)
        # print(quantiles)
        table_p = table[quantiles[table['dataset']].to_numpy() <= table['res'].to_numpy()]

        # normalize: keep p(every module combination) the same
        n_m_all = table_p.groupby(['dataset'] + modelargs).apply(lambda x: len(x))

        n_m_all_smooth = (n_m_all + n_1).apply(lambda x: 0 if np.isnan(x) else x)
        n_m_all = n_m_all_smooth
        #print(n_m_all_smooth)

        p_m_all = (n_m_all / n_all).apply(lambda x: 0 if np.isnan(x) else x)
        nomin = p_m_all.groupby(['dataset']).apply(sum)
        all_distribution = p_m_all / nomin
        #print(all_distribution.to_string())
        # step 3.1. for single module: get information

        stat_table_single = pandas.DataFrame()
        stat_table_single1 = pandas.DataFrame()
        H = {}
        p = {}
        H1 = {}

        for m_arg in modelargs:
            distribution = all_distribution.groupby(['dataset', m_arg]).apply(sum)
            p[m_arg] = distribution
            print("????", m_arg)
            print(distribution.to_string())
            H[m_arg] = distribution.groupby(['dataset']).apply(entropy)
            stat_table_single[m_arg] = H[m_arg]

            H1[m_arg] = distribution.groupby([m_arg]).apply(entropy)
            #print(H1)
            #stat_table_single1[m_arg] = H1[m_arg]



        # print("####################")
        #print(stat_table_single)
        # print("_____________________________________")
        # step 3.2. for two modules
        stat_table_double = pandas.DataFrame()
        stat_table_double1 = pandas.DataFrame()
        I2 = {}
        for i, m_arg0 in enumerate(modelargs):
            for j, m_arg1 in enumerate(modelargs):
                if i <= j:
                    break
                distribution = all_distribution.groupby(['dataset', m_arg0, m_arg1]).apply(sum)



                # dis_div = distribution / p[m_arg0] / p[m_arg1]
                # for dataset in datasets:
                #     print(dis_div[dis_div['dataset'] == dataset].unstack().to_numpy())
                # print("????", m_arg0, m_arg1)
                # print(distribution.to_string())
                # print(n_m_x_y.to_string())
                # print(n_x_y.to_string())
                xy = f'{m_arg0}+{m_arg1}'
                H[xy] = distribution.groupby(['dataset']).apply(scipy.stats.entropy)
                H1[xy] = distribution.groupby([m_arg0, m_arg1]).apply(scipy.stats.entropy)

                stat_table_double[xy] = -H[xy] + H[m_arg0] + H[m_arg1]

                I2[xy] = -H1[xy] + H1[m_arg0] + H1[m_arg1]


        print(H1)
        print(I2)

        # print(stat_table_double)

        p1 = stat_table_single.stack()
        p1.index.set_names(['dataset', 'module'], inplace=True)
        st1 = pandas.DataFrame()
        st1['res'] = p1
        p2 = stat_table_double.stack()
        p2.index.set_names(['dataset', 'modules'], inplace=True)
        st2 = pandas.DataFrame()
        st2['res'] = p2
        st1.reset_index(inplace=True)
        st2.reset_index(inplace=True)

        # draw
        fig = plt.figure()
        sns.barplot(data=st1, x='module', y='res', hue='dataset')
        fig.set_size_inches(18, 8)
        plt.savefig(os.path.join(fig_path, f'combined_single_{int(threshold * 1000)/1000:.3f}.png'))
        plt.close(fig)
        # plt.show()

        fig = plt.figure()
        sns.barplot(data=st2, x='modules', y='res', hue='dataset')
        fig.set_size_inches(18, 8)
        plt.savefig(os.path.join(fig_path, f'combined_double_{int(threshold * 1000)/1000:.3f}.png'))
        plt.close(fig)




def analyse():
    # step 1. open csv
    table = pandas.read_csv(full_csv_path)
    finished = table[table['status'] == 'finished']
    results = {}
    for i, exp in finished.iterrows():
        cmd = CMD(exp['raw_cmd'])
        res = float(exp['result'])
        results[cmd.sorted_cmd_str] = res

    # need only results
    del table
    del finished

    # step 2. open exps
    dirlist = os.listdir(src_dir)
    # step 2.1. find baseline files
    from_all = True
    if from_all:
        all_exps = []
        for k in parse_exps.parse().all():
            all_exps.append(parse_exps.gen_bash(k))
        cmd_set = set(CMD(i).sorted_cmd_str for i in all_exps)
        cmd_list = list(CMD(i) for i in cmd_set)
    else:
        script_prefix1 = 'autogen_sample_script_graph'
        script_prefix2 = 'autogen_sample_script_node'

        script_suffix = '.sh'
        baseline_files = [os.path.join(src_dir, x) for x in dirlist if
                          (x.startswith(script_prefix1) or x.startswith(script_prefix2)) and x.endswith(script_suffix)]
        # step 2.2. read cmd
        cmd_dict = get_cmd(baseline_files)
        print(len(cmd_dict))

        # merge
        cmd_set = set()
        for i in cmd_dict:
            cmd_set.update(cmd_dict[i])
        cmd_list = list(CMD(i) for i in cmd_set)

    # reconstruct table
    table = create_table(cmd_list, results)
    table_smooth = create_table(cmd_list, results, True)

    # table = table[table['dataset'] == 'cora']

    # step 3. analyse

    # mutual information solution

    # get distribution of res: by kde
    # plt.figure()
    # sns.displot(data=table, x="res", hue='dataset', kde=True)
    # plt.show()

    # step 3.0. set threshold for res
    thresholds = np.arange(0.8, 1, 0.2)
    arg_cnt = {m_arg: len(table_smooth[m_arg].value_counts()) for m_arg in modelargs}
    cnt_arg_combination = 1
    for w in arg_cnt.values():
        cnt_arg_combination *= w
    #
    # # create all combinations
    #

    n_all = table.groupby(['dataset'] + modelargs).apply(lambda x: len(x) + 0)
    n_1 = table_smooth.groupby(['dataset'] + modelargs).apply(lambda x: 0)


    # work((table, thresholds, n_all, n_1))
    # multiprocess
    n_split = 20
    with Pool(n_split) as p:
        for _ in tqdm(p.imap_unordered(work, [(table, thresholds[i * len(thresholds) // n_split: (i+1) * len(thresholds) // n_split], n_all, n_1) for i in range(n_split)]), total=n_split):
            continue



    # variance solution (bad)
    # # step 3.1. for single module
    # stat_table = pandas.DataFrame()
    # for m_arg in modelargs:
    #     # print(m_arg)
    #     e = table.groupby(['dataset', m_arg]).mean()
    #     # print(e)
    #     v = e.groupby(['dataset']).var()
    #     stat_table[m_arg] = v['res']
    #     # print(v)
    # print(stat_table)
    #
    # # step 3.2. for two modules
    # for i, m_arg in enumerate(modelargs):
    #     for j, m_arg1 in enumerate(modelargs):
    #         if i <= j:
    #             break
    #         e = table.groupby(['dataset', m_arg, m_arg1]).mean()
    #         v = e.groupby(['dataset', m_arg]).var()
    #         m = v.groupby(['dataset']).mean()
    #         v = e.groupby(['dataset', m_arg1]).var()
    #         m1 = v.groupby(['dataset']).mean()
    #
    #         # v = e.groupby(['dataset']).var()
    #         stat_table[f'{m_arg}+{m_arg1}'] = (m['res'] + m1['res']) / 2
    #
    # #stat_table.to_csv(full_output_path)
    # us = stat_table.unstack()
    # #us.columns =
    #
    # us.to_csv(full_output_path)
    # us = pandas.read_csv(full_output_path)
    # us.columns = ['args', 'dataset', 'res']
    # print(us)
    # for example ... coauthor_cs, est+sampler
    # sns.barplot(data=us, x='args', y='res', hue='dataset')
    # fig = plt.gcf()
    #
    # # Change seaborn plot size
    # fig.set_size_inches(18, 8)
    # plt.show()

if __name__ == '__main__':
    analyse()