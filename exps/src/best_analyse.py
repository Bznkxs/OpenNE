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
from baseline_analyse import getmodel, modelargs, get_model_name1, normalize
from single_analyse import create_table

csv_name = 'failure_analysis.csv'
output_name = 'best_combinations.csv'
output_latex_name = 'best_combinations.tex'
cache_name = 'full_exp_cache.csv'
full_csv_path = os.path.join(processed_dir, csv_name)
full_output_path = os.path.join(processed_dir, output_name)
full_output_latex_path = os.path.join(processed_dir, output_latex_name)
full_cache_path = os.path.join(processed_dir, cache_name)

settings_path = os.path.join(processed_dir, '..', 'settings.json')
fig_path = os.path.join(processed_dir, "..", "graph")

datasets = ['cora', 'citeseer', 'pubmed', 'coauthor_cs', 'coauthor_phy',
            'wikics', 'amazon_photo', 'amazon_computer', 'mutag', 'imdb_binary',
            'imdb_multi', 'reddit_binary', 'ptc_mr']


def analyse():
    # step 1. open csv
    if os.path.exists(full_cache_path):
        table = pandas.read_csv(full_cache_path)
    else:
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
        # step 2.1. find files
        all_exps = []
        for k in parse_exps.parse().all():
            all_exps.append(parse_exps.gen_bash(k))
        cmd_set = set(CMD(i).sorted_cmd_str for i in all_exps)
        cmd_list = list(CMD(i) for i in cmd_set)

        # reconstruct table
        table = create_table(cmd_list, results)
        table.to_csv(full_cache_path)

    table_new = table.sort_values(['task', 'dataset'])
    table_new['task'] = table_new['task'].apply(normalize)
    table_new['rank'] = table_new.groupby(['task', 'dataset'])['res'].rank('min', ascending=False)

    table_new = table_new[table_new['rank'] < 20]
    table_new['model'] = table_new['raw'].apply(get_model_name1)
    table_new = table_new.sort_values(by=['task', 'dataset', 'rank', 'model'])
    table_new = table_new[['task', 'dataset', 'model', 'res']]


    table_new = table_new.set_index(['task', 'dataset'])
    print(table_new)
    table_new.to_csv(full_output_path)
    table_new.to_latex(full_output_latex_path)


if __name__ == '__main__':
    analyse()
