def merge(name, parts):
    w2 = []
    for i in range(parts):
        f2 = open(f"src/{name}_{i}.sh", 'r')
        w2.extend([x for x in f2])
        f2.close()
    print("exps: ",len(w2))
    f2 = open(f"src/{name}.sh", 'w')
    for i in w2:
        f2.write(i)
    f2.close()

if __name__ == '__main__':
    merge("fix_fsn1", 20)