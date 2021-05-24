import json
import os
import random
import sys
from multiprocessing import Pool
from typing import Iterable, Dict, Tuple, List

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
from baseline_analyse import getmodel, modelargs, normalize, in_exp

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
    args = 'dataset,enc,dec,sampler,readout,est,dim,hiddens,task,raw,res'.split(',')
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
        if in_exp(cmd):
            if str(cmd) in results:
                for i in args:
                    wdict[i].append(normalize(cmd.argsdict.get(i, default(i, cmd))))


    table = pandas.DataFrame()
    for a in args:
        table[a] = wdict[a]

    return table


def create_table_2(results):
    args = 'dataset,enc,dec,sampler,readout,est,dim,hiddens,task,raw,res'.split(',')
    def default(arg, c):
        if arg == 'raw':
            return str(c)
        if arg == 'res':
            return results[str(c)]
        return None

    wdict = {a: [] for a in args}
    for cmdstr in results:
        cmd = CMD(cmdstr)
        if in_exp(cmd):
            for i in args:
                wdict[i].append(normalize(cmd.argsdict.get(i, default(i, cmd))))


    table = pandas.DataFrame()
    for a in args:
        table[a] = wdict[a]

    return table


def entropy(it):
    return scipy.stats.entropy(it)


def plot_filled_distribution(distributions, legend, graph_name):
    fig = plt.figure()
    stp = 0.01
    rrr = np.arange(0, 1 + stp, stp)
    sums = [0 * rrr]
    for fi in distributions:
        sums.append(sums[-1] + fi(rrr))
    # div
    divs = []
    for s in sums:
        rx = s / sums[-1]
        divs.append(rx)
    # fill
    for i in range(len(divs) - 1):
        plt.fill_between(rrr, divs[i + 1], divs[i], edgecolor="black")
    plt.legend(legend)
    plt.plot([0, 0], [0, 1], color='black')
    plt.plot([1, 1], [0, 1], color='black')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    fig.set_size_inches(8, 8)
    plt.savefig(os.path.join(fig_path, graph_name))
    plt.close()


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
        #print(len(cmd_dict))

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
    # get option for each m_arg
    options = {}
    for m_arg in modelargs:
        options[m_arg] = list(set(table[m_arg].to_list()))
        options[m_arg].sort()
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

    for ttt in set(table['task'].to_list()):
        print("task =", ttt)
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
        for i, m_arg in enumerate(modelargs):
            print(m_arg, "############")
            table_new1 = table_new
            table_new1 = table_new1.sort_values([m_arg])
            # get kde distributions
            distributions = []
            for option in options[m_arg]:
                print(option, "avg rank =", table_new1[table_new1[m_arg] == option]['rank'].mean())
                f = scipy.stats.gaussian_kde(table_new1[table_new1[m_arg] == option]['rank'])
                distributions.append(f)

            plot_filled_distribution(distributions, options[m_arg], f'single_stack_norm_{ttt}_{m_arg}.png')

        for i, m_arg0 in enumerate(modelargs):
            for j, m_arg1 in enumerate(modelargs):
                if i <= j:
                    break
                print(m_arg0, m_arg1, "############")
                table_new1 = table_new
                table_new1 = table_new1.sort_values([m_arg0, m_arg1])
                # get kde distributions
                distributions = []
                c_options = []
                for option0 in options[m_arg0]:
                    for option1 in options[m_arg1]:
                        f = scipy.stats.gaussian_kde(table_new1[(table_new1[m_arg0] == option0) & (table_new1[m_arg1] == option1)]['rank'])
                        c_options.append(option0 + '+' + option1)
                        distributions.append(f)

                plot_filled_distribution(distributions, c_options, f'dbl_stack_norm_{ttt}_{m_arg0}_{m_arg1}.png')


if __name__ == '__main__':
    analyse()