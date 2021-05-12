import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from pathlib import Path

encoders = ["gcn", "none", "linear", "gat", "gin"]
decoders = ['inner', 'bilinear']
estimators = ["jsd", "nce"]
readouts = ["mean", "sum"]
samplers = ["dgi", "node-neighbor-random", "node-rand_walk-random", "gca", "mvgrl", "aug"]


def getParamsFromSh(line):
    dim = re.findall(r"--dim (.*?) --", line)[0]
    try:
        hiddens = re.findall(r"--hiddens (.*?) --", line)[0].split()
    except:
        hiddens = []
    dec = re.findall(r"--dec (.*?) --", line)[0]
    enc = re.findall(r"--enc (.*?) --", line)[0]
    est = re.findall(r"--est (.*?) --", line)[0]
    readout = re.findall(r"--readout (.*?) --", line)[0]
    sampler = re.findall(r"--sampler (.*?) --", line)[0]
    dataset = re.findall(r"--dataset (.*?) --", line)[0]
    model = re.findall(r"--model (.*?) --", line)[0]
    hidden = ""
    for j in range(0, len(hiddens)):
        hidden += hiddens[j]
    if len(hiddens) == 0:
        hidden = "-"
    return enc, dec, est, readout, hidden, sampler, dataset, dim


def getDataFrame(enc, dec, est, readout, hidden, sampler, dataset, dim):
    s = df[
        (df["enc"] == enc)
        & (df["hiddens"] == hidden)
        & (df["dec"] == dec)
        & (df["est"] == est)
        & (df["readout"] == readout)
        & (df["sampler"] == sampler)
        & (df["dataset"] == dataset)
        & (df["dim"] == int(dim))
        ]
    return s


def get_enc_csv_data(sh_path: str, df: pd.DataFrame):
    file = open(sh_path)
    line = file.readline()
    lines = file.readlines()
    params = ()
    result_dic = {}
    count = 0
    for i in range(0, len(lines)):
        line = lines[i]
        enc, dec, est, readout, hidden, sampler, dataset, dim = getParamsFromSh(line)
        params_1 = (dec, est, readout, sampler, dataset, dim, hidden)

        if params != params_1:
            result_dic[params_1] = {}
            params = params_1
            count = 1
            for i in encoders:
                s = getDataFrame(i, dec, est, readout, hidden, sampler, dataset, dim)

                if len(s) != 0 and s.iloc[0, 8] == "finished":
                    result_1 = float(s.iloc[0, 9])
                    result_dic[params][i] = [result_1]
                else:
                    result_dic[params][i] = [0]
    return result_dic


def get_dec_csv_data(sh_path: str, df: pd.DataFrame):
    file = open(sh_path)
    line = file.readline()
    lines = file.readlines()
    params = ()
    result_dic = {}
    count = 0
    for i in range(0, len(lines)):
        line = lines[i]
        enc, dec, est, readout, hidden, sampler, dataset, dim = getParamsFromSh(line)
        params_1 = (enc, est, readout, sampler, dataset, dim, hidden)

        if params != params_1:
            result_dic[params_1] = {}
            params = params_1
            count = 1
            for i in decoders:
                s = getDataFrame(enc, i, est, readout, hidden, sampler, dataset, dim)

                if len(s) != 0 and s.iloc[0, 8] == "finished":
                    result_1 = float(s.iloc[0, 9])
                    result_dic[params][i] = [result_1]
                else:
                    result_dic[params][i] = [0]
    return result_dic


def get_readout_csv_data(sh_path: str, df: pd.DataFrame):
    file = open(sh_path)
    line = file.readline()
    lines = file.readlines()
    params = ()
    result_dic = {}
    count = 0
    for i in range(0, len(lines)):
        line = lines[i]
        enc, dec, est, readout, hidden, sampler, dataset, dim = getParamsFromSh(line)
        params_1 = (enc, dec, est, sampler, dataset, dim, hidden)

        if params != params_1:
            result_dic[params_1] = {}
            params = params_1
            count = 1
            for i in readouts:
                s = getDataFrame(enc, dec, est, i, hidden, sampler, dataset, dim)

                if len(s) != 0 and s.iloc[0, 8] == "finished":
                    result_1 = float(s.iloc[0, 9])
                    result_dic[params][i] = [result_1]
                else:
                    result_dic[params][i] = [0]
    return result_dic


def get_estimator_csv_data(sh_path: str, df: pd.DataFrame):
    file = open(sh_path)
    line = file.readline()
    lines = file.readlines()
    params = ()
    result_dic = {}
    count = 0
    for i in range(0, len(lines)):
        line = lines[i]
        enc, dec, est, readout, hidden, sampler, dataset, dim = getParamsFromSh(line)
        params_1 = (enc, dec, readout, sampler, dataset, dim, hidden)

        if params != params_1:
            result_dic[params_1] = {}
            params = params_1
            count = 1
            for i in estimators:
                s = getDataFrame(enc, dec, i, readout, hidden, sampler, dataset, dim)

                if len(s) != 0 and s.iloc[0, 8] == "finished":
                    result_1 = float(s.iloc[0, 9])
                    result_dic[params][i] = [result_1]
                else:
                    result_dic[params][i] = [0]
    return result_dic


def get_sampler_csv_data(sh_path: str, df: pd.DataFrame):
    file = open(sh_path)
    line = file.readline()
    lines = file.readlines()
    params = ()
    result_dic = {}
    count = 0
    for i in range(0, len(lines)):
        line = lines[i]
        enc, dec, est, readout, hidden, sampler, dataset, dim = getParamsFromSh(line)
        params_1 = (enc, dec, readout, est, dataset, dim, hidden)

        if params != params_1:
            result_dic[params_1] = {}
            params = params_1
            count = 1
            for i in samplers:
                s = getDataFrame(enc, dec, est, readout, hidden, i, dataset, dim)

                if len(s) != 0 and s.iloc[0, 8] == "finished":
                    result_1 = float(s.iloc[0, 9])
                    result_dic[params][i] = [result_1]
                else:
                    result_dic[params][i] = [0]
    return result_dic


def plotEncRank(data, num, expName):
    my_data = {"enc": [], "rank": []}
    sort = {}
    rank = {}
    for i in encoders:
        sort[i] = [0, 0, 0, 0, 0, 0]
    for i in data:
        dict_0 = data[i]
        dic = sorted(dict_0.items(), key=lambda d: d[1][0], reverse=True)
        current_result = 1.1
        current_comp = 0
        for i in dic:
            if i[1] == current_result:
                sort[i[0]][current_comp] += 1
            else:
                current_result = i[1]
                current_comp += 1
                sort[i[0]][current_comp] += 1
            my_data["enc"].append(i[0])
            my_data["rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    plt.figure(num)
    sns.violinplot(x="enc", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', order=encoders)
    print(sort)
    plt.savefig("../graph/" + expName + ".png")


def plotDecRank(data, num, expName):
    my_data = {"dec": [], "rank": []}
    sort = {}
    rank = {}
    for i in decoders:
        sort[i] = [0, 0, 0]
    for i in data:
        dict_0 = data[i]
        dic = sorted(dict_0.items(), key=lambda d: d[1][0], reverse=True)
        current_result = 1.1
        current_comp = 0
        for i in dic:
            if i[1] == current_result:
                sort[i[0]][current_comp] += 1
            else:
                current_result = i[1]
                current_comp += 1
                sort[i[0]][current_comp] += 1
            my_data["dec"].append(i[0])
            my_data["rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    plt.figure(num)
    sns.violinplot(x="dec", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', )
    print(sort)
    plt.savefig("../graph/" + expName + ".png")


def plotReadoutRank(data, num, expName):
    my_data = {"readout": [], "rank": []}
    sort = {}
    rank = {}
    for i in readouts:
        sort[i] = [0, 0, 0]
    for i in data:
        dict_0 = data[i]
        dic = sorted(dict_0.items(), key=lambda d: d[1][0], reverse=True)
        current_result = 1.1
        current_comp = 0
        for i in dic:
            if i[1] == current_result:
                sort[i[0]][current_comp] += 1
            else:
                current_result = i[1]
                current_comp += 1
                sort[i[0]][current_comp] += 1
            my_data["readout"].append(i[0])
            my_data["rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    plt.figure(num)
    sns.violinplot(x="readout", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', )
    print(sort)
    plt.savefig("../graph/" + expName + ".png")


def plotEstimatorRank(data, num, expName):
    my_data = {"estimator": [], "rank": []}
    sort = {}
    rank = {}
    for i in estimators:
        sort[i] = [0, 0, 0]
    for i in data:
        dict_0 = data[i]
        #print(dict_0)
        dic = sorted(dict_0.items(), key=lambda d: d[1][0], reverse=True)
        current_result = 1.1
        current_comp = 0
        for i in dic:
            if i[1] == current_result:
                sort[i[0]][current_comp] += 1
            else:
                current_result = i[1]
                current_comp += 1
                sort[i[0]][current_comp] += 1
            my_data["estimator"].append(i[0])
            my_data["rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    plt.figure(num)
    sns.violinplot(x="estimator", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', )
    print(sort)
    plt.savefig("../graph/" + expName + ".png")


def plotSamplerRank(data, num, expName):
    my_data = {"sampler": [], "rank": []}
    sort = {}
    rank = {}
    for i in samplers:
        sort[i] = [0, 0, 0, 0, 0, 0, 0]
    for i in data:
        dict_0 = data[i]
        #print(dict_0)
        dic = sorted(dict_0.items(), key=lambda d: d[1][0], reverse=True)
        current_result = 1.1
        current_comp = 0
        for i in dic:
            if i[1] == current_result:
                sort[i[0]][current_comp] += 1
            else:
                current_result = i[1]
                current_comp += 1
                sort[i[0]][current_comp] += 1
            my_data["sampler"].append(i[0])
            my_data["rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    plt.figure(num)
    sns.violinplot(x="sampler", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', order=samplers)
    print(sort)
    plt.savefig("../graph/" + expName + ".png")


# 针对node_enc的版本
df = pd.read_csv("../processed/failure_analysis.csv")
df.columns = df.columns.str.strip()
df.replace('\s+', '', regex=True, inplace=True)
data = get_enc_csv_data("../../src/autogen_sample_script_node_enc.sh", df)
plotEncRank(data, 1, "node_enc")
data = get_enc_csv_data("../../src/autogen_sample_script_graph_enc.sh", df)
plotEncRank(data, 2, "graph_enc")

data = get_dec_csv_data("../../src/autogen_sample_script_graph_dec.sh", df)
plotDecRank(data, 3, "graph_dec")
data = get_dec_csv_data("../../src/autogen_sample_script_node_dec.sh", df)
plotDecRank(data, 4, "node_dec")

data = get_readout_csv_data("../../src/autogen_sample_script_graph_readout.sh", df)
plotReadoutRank(data, 5, "graph_readout")
data = get_readout_csv_data("../../src/autogen_sample_script_node_readout.sh", df)
plotReadoutRank(data, 6, "node_readout")

data = get_estimator_csv_data("../../src/autogen_sample_script_graph_est.sh", df)
plotEstimatorRank(data, 7, "graph_est")
data = get_estimator_csv_data("../../src/autogen_sample_script_node_est.sh", df)
plotEstimatorRank(data, 8, "node_est")

data = get_sampler_csv_data("../../src/autogen_sample_script_graph_sampler.sh", df)
plotSamplerRank(data, 9, "graph_sampler")
data = get_sampler_csv_data("../../src/autogen_sample_script_node_sampler.sh", df)
plotSamplerRank(data, 10, "node_sampler")
