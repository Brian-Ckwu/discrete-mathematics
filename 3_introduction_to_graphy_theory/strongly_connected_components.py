import networkx as nx

if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd'), ('e', 'd'), ('f', 'a'), ('b', 'f')])
    print("Strongly connected components:")
    sccs = list()
    for scc in nx.strongly_connected_components(G):
        sccs.append(scc)
    print(sccs)