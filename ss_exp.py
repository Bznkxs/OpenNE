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


test_list = {
    "model": ["ss_nodemodel"],
    "dataset": ["cora"],
    "enc": ["none", "gcn", "gat", "gin", "linear"],
    "dec": ["inner", "bilinear", "mlp"],
    "sampler": sampler_list,
    "readout": ["mean"],
    "est": ["jsd"],
    "epochs": ["1"],
    "early-stopping": ["20"],

    "dim": ["16",],
    "_hiddens": [0],
    "lr": ["0.001"],

}

basics_bat = "python -m openne"
basics_bash = "python3 -m openne"

ll = []
def rec(reclist, idea, dim=None, format='bat'):
    if len(reclist) == 0:
        if format == 'bat':
            ll.append(idea + " %1 %2 %3 %4 %5 %6 %7 %8 %9")
        else:
            ll.append(idea + " $*")
        return
    l, r = reclist[0]

    if l == "_hiddens":
        rec(reclist[1:], idea)
        for p in r[1:]:
            elist = ' '.join([dim]*p)
            rec(reclist[1:], idea + ' --hiddens ' + elist, dim, format)
        return
    for p in r:
        if l == "dim":
            dim = p
        rec(reclist[1:], idea + " --" + l + " " + p, dim, format)

def rec0(reclist, idea, dim=None, format='bat'):
    # inits
    ll.clear()
    rec(reclist, idea, dim, format=format)

import random

pos = 0.2
training_list = list(training_list.items())
test_list = list(test_list.items())

def gen_exps(glist, name):
    ll.clear()
    filename1 = os.path.join(os.path.dirname(__file__), f"src/{name}_{pos}.bat")
    print(filename1)
    filename2 = os.path.join(os.path.dirname(__file__), f"src/{name}_{pos}.sh")
    print(filename2)
    with open(filename1, "w") as f1:
        rec0(glist, basics_bat, "bat")
        for l in ll:
            if random.random() < pos:
                print(l, file=f1)
    ll.clear()
    with open(filename2, "w") as f2:

        rec0(glist, basics_bash, "bash")
        for l in ll:
            if random.random() < pos:
                print(l, file=f2)


if __name__ == "__main__":
    gen_exps(training_list, 'ss_node')
    gen_exps(test_list, 'test')






