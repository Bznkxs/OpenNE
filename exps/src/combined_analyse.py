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
from single_analyse import create_table

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



def entropy(it):
    return scipy.stats.entropy(it)
    # res = 0
    # ans = 1
    # for x in it:

def work0(args):
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



        # print("####################")
        #print(stat_table_single)
        # print("_____________________________________")
        # step 3.2. for two modules
        stat_table_double = pandas.DataFrame()
        stat_table_double1 = pandas.DataFrame()
        I2 = {}
        p2 = {}

        for i, m_arg0 in enumerate(modelargs):
            for j, m_arg1 in enumerate(modelargs):
                if i <= j:
                    break
                distribution = all_distribution.groupby(['dataset', m_arg0, m_arg1]).apply(sum)



                xy = f'{m_arg0}+{m_arg1}'
                H[xy] = distribution.groupby(['dataset']).apply(scipy.stats.entropy)
                H1[xy] = distribution.groupby([m_arg0, m_arg1]).apply(scipy.stats.entropy)

                stat_table_double[xy] = -H[xy] + H[m_arg0] + H[m_arg1]
                I2[xy] = -H1[xy] + H1[m_arg0] + H1[m_arg1]

                p2[xy] = distribution / p[m_arg0] - p[m_arg1]
                p2[f'{m_arg1}+{m_arg0}'] = distribution / p[m_arg1] - p[m_arg0]



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

def work(args):
    table_0, thresholds, n_all, n_1, options, module_names, module_no_dict, module_intv = args
    for ttt in set(table_0['task'].to_list()):
        print(ttt)
        table = table_0[table_0['task'] == ttt]
        for threshold in thresholds:
            quantiles = table.groupby('dataset')['res'].quantile(threshold)
            table_p = table[quantiles[table['dataset']].to_numpy() <= table['res'].to_numpy()]

            # normalize: keep p(every module combination) the same
            n_m_all = table_p.groupby(modelargs).apply(lambda x: len(x))

            n_m_all_smooth = (n_m_all + n_1).apply(lambda x: 0 if np.isnan(x) else x)
            n_m_all = n_m_all_smooth

            p_m_all = (n_m_all / n_all).apply(lambda x: 0 if np.isnan(x) else x)
            nomin = sum(p_m_all)
            all_distribution = p_m_all / nomin
            print(all_distribution)
            print(nomin)
            print(all_distribution[all_distribution > 0.])
            print(sum(all_distribution))
            # step 3.1. for single module: get information

            p = {}

            for m_arg in modelargs:
                distribution = all_distribution.groupby([m_arg]).apply(sum)
                p[m_arg] = distribution
                print(distribution)


            # step 3.2. for two modules
            heatmap = np.zeros([len(module_names), len(module_names)])
            heatmap[:, :] = np.nan
            for i, m_arg0 in enumerate(modelargs):
                for j, m_arg1 in enumerate(modelargs):
                    if i <= j:
                        break
                    distribution = all_distribution.groupby([m_arg0, m_arg1]).apply(sum)

                    mxr = distribution / p[m_arg0] - p[m_arg1]
                    mxr = mxr.unstack(m_arg1)
                    mat1 = mxr.to_numpy()
                    mxl = distribution / p[m_arg1] - p[m_arg0]
                    mxl = mxl.unstack(m_arg0)
                    mat2 = mxl.to_numpy()
                    print(mxr)

                    heatmap[module_intv[m_arg0], module_intv[m_arg1]] = mat1
                    heatmap[module_intv[m_arg1], module_intv[m_arg0]] = mat2

            heatmap_df = pandas.DataFrame(heatmap)
            heatmap_df.columns = module_names
            heatmap_df.index = module_names
            print(heatmap_df)

            fig = plt.figure()
            fig.set_size_inches(12,12)

            sns.heatmap(heatmap_df, square=True).set_title(f"task {ttt}: heatmap of $p(x|y)-y$")

            plt.show()




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
    from_all = False
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
    thresholds = np.arange(0.9, 1, 0.2)
    arg_cnt = {m_arg: len(table_smooth[m_arg].value_counts()) for m_arg in modelargs}
    cnt_arg_combination = 1
    for w in arg_cnt.values():
        cnt_arg_combination *= w
    #
    # # create all combinations
    #

    n_all = table.groupby(['dataset'] + modelargs).apply(lambda x: len(x) + 0)
    n_1 = table_smooth.groupby(['dataset'] + modelargs).apply(lambda x: 0)
    options = {}
    module_names = []
    module_no_dict = {}
    module_intv = {}
    for m_arg in modelargs:
        options[m_arg] = list(set(table[m_arg].to_list()))
        options[m_arg].sort()
        x_st = len(module_names)
        x_ed = x_st + len(options[m_arg])
        module_intv[m_arg] = slice(x_st, x_ed)
        for opt in options[m_arg]:
            module_no_dict[opt] = len(module_names)

            module_names.append(opt)

    work((table, thresholds, n_all, n_1, options, module_names, module_no_dict, module_intv))
    # multiprocess
    # n_split = 20
    # with Pool(n_split) as p:
    #     for _ in tqdm(p.imap_unordered(work, [(table, thresholds[i * len(thresholds) // n_split: (i+1) * len(thresholds) // n_split], n_all, n_1) for i in range(n_split)]), total=n_split):
    #         continue






    for ttt in set(table['task'].to_list()):
        print(ttt)
        table_new = table[table['task'] == ttt]
        table_new = table_new.sort_values(['dataset'])
        table_new['rank'] = table_new.groupby(['dataset'])['res'].rank('min', ascending=False)
        #print(table_new[['dataset', 'enc', 'res', 'rank']].sort_values(['dataset', 'enc', 'res', 'rank']).to_string())
        q = table_new.groupby(['dataset'])['res'].size()
        table_new = table_new.set_index(['dataset'] + modelargs)

        table_new['rank'] = table_new['rank'] / q

        table_new.reset_index(inplace=True)
        table_new['rank'] = table_new['rank'].rank(method='min')
        q = len(table_new)
        table_new['rank'] = table_new['rank'] / q

        heatmap = np.zeros([len(module_names), len(module_names)])
        heatmap[:, :] = np.nan
        for i, m_arg0 in enumerate(modelargs):
            for j, m_arg1 in enumerate(modelargs):
                if i <= j:
                    break
                # fill heatmap
                # value: best rank
                mxr = table_new.groupby([m_arg0, m_arg1])['rank'].min()

                #print(mxr)
                # mxr = mxr.reset_index()
                mxr = mxr.unstack(m_arg1)
                mat = mxr.to_numpy()
                heatmap[module_intv[m_arg0], module_intv[m_arg1]] = mat
                heatmap[module_intv[m_arg1], module_intv[m_arg0]] = mat.T
                # print(mxr)

        heatmap = heatmap ** 0.25
        #print(heatmap)
        heatmap_df = pandas.DataFrame(heatmap)
        heatmap_df.columns = module_names
        heatmap_df.index = module_names
        #print(heatmap_df)

        fig = plt.figure()
        fig.set_size_inches(12,12)

        sns.heatmap(heatmap_df, square=True).set_title(f"task {ttt}: heatmap of $\\min(rank)^{{0.25}}$")
        plt.show()
        plt.close()




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