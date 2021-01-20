f1 = open("src/ss_node_0.2.sh", 'r')
f2 = open("src/ss_node_1.sh", 'r')
w = []
w2 = [x for x in f2]
print(len(w2), "exps")
f1.close()
f2.close()
M = 20
w2 = [x for x in w2 if x not in w]
print("after removing suspicious files: ",len(w2))
size = int(len(w2) / M + 0.5)
for m in range(M):
    w3 = w2[m * size : (m+1) * size]
    print((m+1)*size)
    f2 = open(f"src/ss_node_1_{m}.sh", 'w')
    for i in w3:
        f2.write(i)
    f2.close()