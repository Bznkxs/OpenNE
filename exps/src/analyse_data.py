import numpy as np
import pandas as pd
import re

#针对node_dec的版本
df = pd.read_csv("../processed/failure_analysis.csv")
df.columns = df.columns.str.strip()
df.replace('\s+','',regex=True,inplace=True)
file = open("../../src/autogen_sample_script_node_dec.sh")
line = file.readline()
lines = file.readlines()
rank_1 = []
rank_2 = []
compare_1 = [0, 0]
compare_2 = [0, 0]

i = 0
for i in range(0, len(lines)):
    line = lines[i]
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
    if i % 2 == 0:
        if len(s) != 0 and s.iloc[0, 8] == "finished":
            result_1 = float(s.iloc[0, 9])
            rank_1.append(result_1)
        else:
            rank_1.append("")
    else:
        if len(s) != 0 and s.iloc[0, 8] == "finished":
            result_1 = float(s.iloc[0, 9])
            rank_2.append(result_1)
        else:
            rank_2.append("")
        len_2 = len(rank_1) - 1
        if (rank_1[len_2] != "") and (rank_2[len_2] != ""):
            if rank_2[len_2] > rank_1[len_2]:
                compare_1[1] += 1
                compare_2[0] += 1
            elif rank_1[len_2] > rank_2[len_2]:
                compare_1[0] += 1
                compare_2[1] += 1
            else:
                compare_1[0] += 1
                compare_2[0] += 1
    i += 1

print(compare_1)
print(compare_2)

print(rank_1)
print(rank_2)
