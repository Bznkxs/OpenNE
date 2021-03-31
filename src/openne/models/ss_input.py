class model_input:
    GRAPHS = "graphs"
    NODES = "nodes"
    TYPES = [GRAPHS, NODES]

    def __init__(self, typ, adj, start_idx, feature, repeat=False, num_graphs=1, actual_indices=None):
        """
        batch graph input
        @param typ: "graphs"/"nodes"
        @param graphs: a collection
        @param feature: collection of feat
        @param repeat: (only for typ graphs) if True, embedding of graph will be repeated (num_node) times
        """
        self.typ = typ
        assert self.typ in self.TYPES
        self.adj = adj
        self.start_idx = start_idx
        self.feat = feature
        self.repeat = repeat
        self.num_graphs = num_graphs
        self.actual_indices = actual_indices