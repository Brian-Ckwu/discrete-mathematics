import networkx as nx
from nxpd import draw, nxpdParams

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'c'), (2, 'e'), (3, 'b'),
                    (3, 'c'), (3, 'd'), (4, 'a'), (4, 'e'), (5, 'a'), (5, 'e')])
    if nx.bipartite.is_bipartite(G):
        print("This graph is bipartite.")
    else:
        print("This graph is not bipartite.")
        exit()
    M = nx.max_weight_matching(G)
    print(M)