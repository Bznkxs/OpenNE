import json
import copy
import os


data_path = os.path.join(os.path.dirname(__file__), "../settings.json")

class HashableDict(dict):
    def __hash__(self):
        return str(self).__hash__()

def cartesian_prod(grids, name=''):
    keys = list(grids.keys())
    res = set()
    def dfs(fruit, depth = 0):
        if depth == len(keys):
            res.add(fruit)
            return
        key = keys[depth]

        for opt in grids[key]:
            newfruit = copy.deepcopy(fruit)
            newfruit[key] = opt
            dfs(newfruit, depth+1)
    dfs(HashableDict())
    return res

class ExpVariable:
    def __init__(self, data, name='root'):
        self.name = name
        self.data = data
        self.vars = {}
        self.opt_groups = {}
        self.parse()

    def all(self):
        ret = set()
        for k, v in self.opt_groups.items():
            #print("--all ", k)
            ret = ret.union(v)
        return ret

    def select(self, set_of_opt_groups):
        ret = set()
        for k, v in self.opt_groups.items():
            if k in set_of_opt_groups:
                #print("--select ", v)
                ret = ret.union(v)
        return ret

    def parse_options(self, data):
        for k, v in data.items():
            self.opt_groups[k] = set()
            if isinstance(v, list):  # a simple opt group
                self.opt_groups[k] = self.opt_groups[k].union(set(v))
            else: # a generation rule
                # print(k, v)
                # parse this rule
                grids = {}
                for var, grps in v.items():  # select groups of var
                    if grps == 'all':
                        grids[var] = self.vars[var].all()
                    else:  # selected groups
                        grids[var] = self.vars[var].select(set(grps))
                for var in self.vars.keys():  # omitted
                    if var not in grids:
                        grids[var] = self.vars[var].all()
                self.opt_groups[k] = cartesian_prod(grids, k)



    def parse(self):
        for k, v in self.data.items():
            if k == '_options':  # options
                # print(self.name, list(self.vars.keys()))
                self.parse_options(v)
                continue
            # variable
            self.vars[k] = ExpVariable(v, name=k)
        # print(self)

    def __str__(self):
        space = '\n        '
        s = '\n\n'.join([
            f"name:   {self.name}",
            f"vars:   {space.join(self.vars.keys())}",
            f"opts:   {space.join([k + ': ' + str(len(self.opt_groups[k])) for k in self.opt_groups.keys()])}"
        ])
        return '------VAR-------\n' + s + '\n-------VAR-------\n'

def parse():
    with open(file=data_path, mode='r') as fp:
        data = json.load(fp)
        ret = ExpVariable(data)
        return ret

def gen_bash(opt):
    s = "python3 -m openne"
    def dfs(opt):
        res = ''
        flg = -1
        dim = '1'
        keys = list(opt.keys())
        # sorted_keys = keys.sort(key=lambda x: )
        for k in keys:
            v = opt[k]
            if k.startswith('_'):
                if isinstance(v, dict):
                    res += dfs(v)
                elif k == '_hiddens':
                    flg = v
            else:
                if k == 'dim':
                    dim = v
                res += ' --' + k + ' ' + v
        if flg > 0:
            res += ' --hiddens'
            for i in range(flg):
                res += ' ' + dim
        return res

    s += dfs(opt) + " $*"
    return s


if __name__ == "__main__":
    exps = parse()
    print(exps)
    for i in exps.opt_groups["node_node"]:
        print(str(i))
        print(gen_bash(i))
        break
