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

    "dim": ["64", "128", "256"],
    "_hiddens": [0,1,2],
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
def rec(reclist, idea, dim=None, form='bat'):
    if len(reclist) == 0:

        if form == 'bat':
            ll.append(idea + " %1 %2 %3 %4 %5 %6 %7 %8 %9")
        else:
            ll.append(idea + " $*")
        return
    l, r = reclist[0]

    if l == "_hiddens":
        rec(reclist[1:], idea, dim=dim, form=form)
        for p in r[1:]:
            elist = ' '.join([dim]*p)
            rec(reclist[1:], idea + ' --hiddens ' + elist, dim=dim, form=form)
        return
    for p in r:
        if l == "dim":
            dim = p
        rec(reclist[1:], idea + " --" + l + " " + p, dim=dim, form=form)

def rec0(reclist, idea, dim=None, form='bat'):
    # inits
    ll.clear()
    rec(reclist, idea, dim=dim, form=form)

import random

pos = 1
training_list = list(training_list.items())
test_list = list(test_list.items())

def gen_exps(glist, name, mode='w'):
    ll.clear()
    filename1 = os.path.join(os.path.dirname(__file__), f"src/{name}_{pos}.bat")
    print(filename1)
    filename2 = os.path.join(os.path.dirname(__file__), f"src/{name}_{pos}.sh")
    print(filename2)
    with open(filename1, mode) as f1:
        rec0(glist, basics_bat, form= "bat")
        for l in ll:
            if random.random() < pos:
                print(l, file=f1)
    ll.clear()
    with open(filename2, mode) as f2:

        rec0(glist, basics_bash, form="bash")
        for l in ll:
            if random.random() < pos:
                print(l, file=f2)

training_list2 = list({
    "model": ["ss_nodemodel"],
    "dataset": ["cora", "citeseer", "pubmed"],
    "enc": ["gat"],
    "dec": ["inner", "bilinear", "mlp"],
    "sampler": sampler_list,
    "readout": ["mean"],
    "est": ["jsd"],
    "epochs": ["500"],
    "early-stopping": ["20"],

    "dim": ["64", "128", "256"],
    "_hiddens": [0,1,2],
    "lr": ["0.001", "0.01", "0.02", "0.03"],
}.items())

new_sampler_list = ["dgi", "mvgrl"]

graph_samplers = [["graph"], ["node", "diffusion"], ["permuted"]]

# for i in node_samplers[0]:
#     for j in node_samplers[1]:
#         for k in node_samplers[2]:
#             new_sampler_list.append(i+"-"+j+"-"+k)

training_list3 = list({
    "model": ["ss_gae"],
    "dataset": ["cora", "citeseer", "pubmed"],
    "enc": ["gin", "gcn", "gat"],
    "dec": ["inner", "bilinear", "mlp"],
    "sampler": new_sampler_list,
    "readout": ["mean"],
    "est": ["jsd"],
    "epochs": ["500"],
    "early-stopping": ["20"],
    "dim": ["64", "128", "256"],
    "_hiddens": [0,1,2],
    "lr": ["0.001", "0.01", "0.02", "0.03"],
}.items())

training_list4 = list({
    "model": ["ss_gaeg"],
    "task": ['graphclassification'],
    "dataset": ["mutag", "imdb_binary", "imdb_multi", "reddit_binary", "ptc_mr", ],
    "enc": ["gin", "gcn", "gat"],
    "dec": ["inner", "bilinear", "mlp"],
    "sampler": new_sampler_list,
    "readout": ["mean", 'sum'],
    "est": ["jsd", 'nce'],
    "epochs": ["500"],
    "early-stopping": ["20"],
    "dim": ["32", "64",],
    "_hiddens": [0,1,2],
    "lr": ["0.001", "0.01" ],
    'clf-ratio': ['0.8'],
    'patience': ['3']
}.items())

if __name__ == "__main__":
    gen_exps(training_list, 'ss_node')
    gen_exps(training_list2, 'ss_gat')
    gen_exps(training_list3, 'ss_graph')
    gen_exps(training_list4, 'ss_graphs')
    #pos = 1
    #gen_exps(test_list, 'test')






