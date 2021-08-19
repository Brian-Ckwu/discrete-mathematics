import networkx as nx

def create_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a'),
                    ('f', 'a'), ('g', 'b'), ('h', 'c'), ('i', 'd'), ('j', 'e'), 
                    ('f', 'h'), ('h', 'j'), ('j', 'g'), ('g', 'i'), ('i', 'f'),
                    ('j', 'i'), ('j', 'd'), ('d', 'g')])
    return G

def find_maximum_clique(G: nx.Graph) -> list:
    cliques = nx.find_cliques(G)
    max_clique = []
    for c in cliques:
        if (len(c) > len(max_clique)):
            max_clique = c
    return max_clique

if __name__ == "__main__":
    G = create_graph()
    max_clique = find_maximum_clique(G)
    print(max_clique)