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
encoderOrder = ["GCN", "lookup", "MLP", "GAT", "GIN",]
encName = {
    "gcn": "GCN",
    "none": "lookup",
    "linear": "MLP",
    "gat": "GAT",
    "gin": "GIN",
}
decName = {
    "inner": "inner product",
    "bilinear": "bilinear",
}
estName = {
    "jsd": "JSD",
    "nce": "InfoNCE"
}
readoutName = {
    "mean": "mean",
    "sum": "sum",
}
samplerName = {
    "dgi": "DGI",
    "mvgrl": "MVGRL",
    "aug": "GCL",
    "gca": "GCA",
    "node-neighbor-random": "LINE",
    "node-rand_walk-random": "DW",
}


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
                    result_1 = int(float(s.iloc[0, 9]) * 100)
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
                    result_1 = int(float(s.iloc[0, 9]) * 100)
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
                    result_1 = int(float(s.iloc[0, 9]) * 100)
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
                    result_1 = int(float(s.iloc[0, 9]) * 100)
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
                    result_1 = int(float(s.iloc[0, 9]) * 100)
                    result_dic[params][i] = [result_1]
                else:
                    result_dic[params][i] = [0]
    return result_dic


def plotEncRank(data, num, expName):
    my_data = {"Encoder": [], "Rank": []}
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
            my_data["Encoder"].append(encName[i[0]])
            my_data["Rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    df_0 = df_0.sort_values(by=["Encoder", "Rank"], ascending=[True,True])
    sns.set(font_scale=2)
    plt.figure(num + 10)
    fig, ax = plt.subplots(2,1,figsize=[9.6, 10])
    # sns.violinplot(x="enc", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', order=encoders)
    ax[0].set(ylim=(1,5))
    ax[0].set_yticks(np.arange(1,6,1))
    g = sns.barplot(data=df_0, x="Encoder", y="Rank", ax=ax[0])
    g.set(xticklabels=[], xlabel=None)
    '''
    plt.tight_layout()
    plt.savefig("../graph/" + expName + "_bar.png")
    plt.close()

    plt.figure(num)
    '''
    # sns.violinplot(x="enc", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', order=encoders)
    #sns.set_style("white")
    current_palette = sns.color_palette()
    ax[1].set(ylim=(0,100))
    sns.histplot(data=df_0, x="Encoder", hue="Rank", multiple="stack", shrink=.8, legend=False, hue_order=[5,4,3,2,1],
                 palette=sns.color_palette("mako_r", n_colors=5), ax=ax[1])
    print(sort)
    plt.tight_layout()
    plt.savefig("../graph/" + expName + ".png")
    plt.close()


def plotDecRank(data, num, expName):
    my_data = {"Decoder": [], "Rank": []}
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
            my_data["Decoder"].append(i[0])
            my_data["Rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    df_0 = df_0.sort_values("Decoder")
    sns.set(font_scale=2)
    plt.figure(num)
    fig, ax = plt.subplots(2,1,figsize=[4.8, 10])
    '''
    plt.figure(figsize=(8, 6))
    fig, axes = plt.subplots(1, 2)
    '''
    d = sns.histplot(data=df_0, x="Decoder", hue="Rank", multiple="stack", shrink=.8, legend=False, hue_order=[2,1],
                 palette=sns.color_palette(palette="mako_r", n_colors=2), ax=ax[1])
    print(sort)
    ax[1].set(ylim=(0,100))
    '''
    plt.tight_layout()
    plt.savefig("../graph/" + expName + "_dis.png")

    plt.figure(num + 10)
    '''
    ax[0].set(ylim=(1, 2))
    g = sns.barplot(data=df_0, x="Decoder", y="Rank", ax=ax[0])
    ax[0].set_yticks(np.arange(1,3,1))
    g.set(xticklabels=[], xlabel=None)
    d.set(ylabel=None)
    g.set(ylabel=None)
    plt.tight_layout()
    plt.savefig("../graph/" + expName + ".png")
    plt.close()


def plotReadoutRank(data, num, expName):
    my_data = {"Readout": [], "Rank": []}
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
            my_data["Readout"].append(i[0])
            my_data["Rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    df_0 = df_0.sort_values("Readout")
    sns.set(font_scale=2)
    plt.figure(num)
    fig, ax = plt.subplots(2,1,figsize=[4.8, 10])
    '''
    plt.figure(figsize=(8, 6))
    fig, axes = plt.subplots(1, 2)
    '''
    d = sns.histplot(data=df_0, x="Readout", hue="Rank", multiple="stack", shrink=.8, legend=False, hue_order=[2,1],
                 palette=sns.color_palette(palette="mako_r", n_colors=2), ax=ax[1])
    print(sort)
    ax[1].set(ylim=(0,100))
    '''
    plt.tight_layout()
    plt.savefig("../graph/" + expName + "_dis.png")

    plt.figure(num + 10)
    '''
    ax[0].set(ylim=(1, 2))
    g = sns.barplot(data=df_0, x="Readout", y="Rank", ax=ax[0])
    ax[0].set_yticks(np.arange(1,3,1))
    g.set(xticklabels=[], xlabel=None)
    d.set(ylabel=None)
    g.set(ylabel=None)
    plt.tight_layout()
    plt.savefig("../graph/" + expName + ".png")
    plt.close()


def plotEstimatorRank(data, num, expName):
    my_data = {"Estimator": [], "Rank": []}
    sort = {}
    rank = {}
    for i in estimators:
        sort[i] = [0, 0, 0]
    for i in data:
        dict_0 = data[i]
        # print(dict_0)
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
            my_data["Estimator"].append(estName[i[0]])
            my_data["Rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    df_0 = df_0.sort_values("Estimator")
    sns.set(font_scale=2)
    plt.figure(num)
    fig, ax = plt.subplots(2,1,figsize=[4.8, 10])
    d = sns.histplot(data=df_0, x="Estimator", hue="Rank", multiple="stack", shrink=.8, legend=False, hue_order=[2,1],
                 palette=sns.color_palette(palette="mako_r", n_colors=2), ax=ax[1])
    d.set(ylabel=None)
    print(sort)
    ax[1].set(ylim=(0,100))
    '''
    plt.tight_layout()
    plt.savefig("../graph/" + expName + "_dis.png")

    plt.figure(num + 10)
    '''
    ax[0].set(ylim=(1, 2))
    g = sns.barplot(data=df_0, x="Estimator", y="Rank", ax=ax[0])
    ax[0].set_yticks(np.arange(1,3,1))
    g.set(xticklabels=[], xlabel=None)
    g.set(ylabel=None)
    plt.tight_layout()
    plt.savefig("../graph/" + expName + ".png")
    plt.close()


def plotSamplerRank(data, num, expName):
    my_data = {"Sampler": [], "Rank": []}
    sort = {}
    rank = {}
    for i in samplers:
        sort[i] = [0, 0, 0, 0, 0, 0, 0]
    for i in data:
        dict_0 = data[i]
        # print(dict_0)
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
            my_data["Sampler"].append(samplerName[i[0]])
            my_data["Rank"].append(current_comp)
    df_0 = pd.DataFrame(my_data)
    #df_0 = df_0.sort_values("Sampler")
    df_0 = df_0.sort_values(by=["Sampler", "Rank"], ascending=[True,True])
    sns.set(font_scale=2)
    plt.figure(num + 10, figsize=[9.6, 20])
    fig, ax = plt.subplots(2,1,figsize=[9.6, 10])
    # sns.violinplot(x="enc", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', order=encoders)
    ax[0].set(ylim=(1,5))
    g = sns.barplot(data=df_0, x="Sampler", y="Rank", ax=ax[0])
    g.set(xticklabels=[], xlabel=None)

    '''
    plt.tight_layout()
    plt.savefig("../graph/" + expName + "_bar.png")
    plt.close()

    plt.figure(num)
    '''
    # sns.violinplot(x="enc", y='rank', data=df_0, linewidth=2, width=0.8, palette='muted', order=encoders)
    #sns.set_style("white")
    current_palette = sns.color_palette()
    ax[1].set(ylim=(0,100))
    d = sns.histplot(data=df_0, x="Sampler", hue="Rank", multiple="stack", shrink=.8, legend=False, hue_order=[6,5,4,3,2,1],
                 palette=sns.color_palette("mako_r", n_colors=6), ax=ax[1])
    print(sort)
    d.set(ylabel=None)
    g.set(ylabel=None)
    plt.tight_layout()
    plt.savefig("../graph/" + expName + ".png")
    plt.close()


# 针对node_enc的版本
df = pd.read_csv("../processed/failure_analysis.csv")
df.columns = df.columns.str.strip()
df.replace('\s+', '', regex=True, inplace=True)
data = get_enc_csv_data("../../src/autogen_sample_script_graph_enc.sh", df)
plotEncRank(data, 2, "graph_enc")
data = get_enc_csv_data("../../src/autogen_sample_script_node_enc.sh", df)
plotEncRank(data, 1, "node_enc")

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
