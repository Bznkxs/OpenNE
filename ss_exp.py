import os
sampler_list = []

node_samplers = [["node"], ["neighbor", "rand_walk"], ["random", "except_neighbor"]]

for i in node_samplers[0]:
    for j in node_samplers[1]:
        for k in node_samplers[2]:
            sampler_list.append(i+"-"+j+"-"+k)

training_list = {
    "model": ["ss_nodemodel"],
    "dataset": ["cora", "citeseer", "pubmed"],
    "enc": ["none", "gcn", "gat", "gin", "linear"],
    "dec": ["inner", "bilinear", "mlp"],
    "sampler": sampler_list,
    "readout": ["mean"],
    "est": ["jsd"],
    "epochs": ["500"],
    "early-stopping": ["20"],

    "dim": ["64", "128", "256", "512"],
    "_hiddens": [0,1,2,3],
    "lr": ["0.001", "0.01", "0.02", "0.03"],

}
basics_bat = "python -m openne"
basics_bash = "python3 -m openne"

ll = []
def rec(reclist, idea, dim=None):
    if len(reclist) == 0:
        ll.append(idea)
        return
    l, r = reclist[0]

    if l == "_hiddens":
        rec(reclist[1:], idea)
        for p in r[1:]:
            elist = ' '.join([dim]*p)
            rec(reclist[1:], idea + ' --hiddens ' + elist)
        return
    for p in r:
        if l == "dim":
            dim = p
        rec(reclist[1:], idea + " --" + l + " " + p, dim)

import random

pos = 0.2




if __name__ == "__main__":
    training_list = list(training_list.items())

    filename1 = os.path.join(os.path.dirname(__file__), f"src/ss_node_{pos}.bat")
    print(filename1)
    filename2 = os.path.join(os.path.dirname(__file__), f"src/ss_node_{pos}.sh")
    print(filename2)
    with open(filename1, "w") as f1:
        rec(training_list, basics_bat)
        for l in ll:
            if random.random() < pos:
                print(l, file=f1)
    ll = []
    with open(filename2, "w") as f2:

        rec(training_list, basics_bash)
        for l in ll:
            if random.random() < pos:
                print(l, file=f2)



