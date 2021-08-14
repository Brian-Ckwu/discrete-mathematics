import networkx as nx

if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd')])
    if nx.is_directed_acyclic_graph(G):
        print("Topological ordering of the nodes:", list(nx.topological_sort(G)))
    else:
        print("G contains a cycle, hence it cannot be topologically sorted.")