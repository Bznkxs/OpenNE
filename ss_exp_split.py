from sys import argv


def split(name, parts):
    f2 = open(f"src/{name}.sh", 'r')
    w = []  # suspicious files to remove
    w2 = [x for x in f2]
    print(len(w2), "exps")
    f2.close()
    M = parts
    w2 = [x for x in w2 if x not in w]
    print("after removing suspicious files: ", len(w2))
    import random
    random.shuffle(w2)
    size = int(len(w2) / M + 0.5)
    for m in range(M):
        w3 = w2[m * size: (m + 1) * size]
        print((m + 1) * size)
        f2 = open(f"src/{name}_{m}.sh", 'w')
        f2.write("#!/bin/sh\n")
        for i in w3:
            f2.write(i)
        f2.close()


if __name__ == '__main__':
    # split("ss_gat_1", 5)
    # split("ss_graph_1", 5)
    # split("fix_fsn", 3)
    # split("ss_graphs2_1", 3)
    if len(argv) == 1:
        split("autogen_script", 3)
    elif len(argv) == 2:
        split(argv[1], 3)
    else:
        split(argv[1], int(argv[2]))

# f1 = open("src/ss_node_0.2.sh", 'r')
# f2 = open("src/ss_node_1.sh", 'r')
# w = []
# w2 = [x for x in f2]
# print(len(w2), "exps")
# f1.close()
# f2.close()
# M = 20
# w2 = [x for x in w2 if x not in w]
# print("after removing suspicious files: ",len(w2))
# size = int(len(w2) / M + 0.5)
# for m in range(M):
#     w3 = w2[m * size : (m+1) * size]
#     print((m+1)*size)
#     f2 = open(f"src/ss_node_1_{m}.sh", 'w')
#     for i in w3:
#         f2.write(i)
#     f2.close()
