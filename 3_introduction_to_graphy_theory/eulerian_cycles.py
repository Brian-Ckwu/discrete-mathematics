import networkx as nx

if __name__ == "__main__":
    # construct a graph
    G = nx.DiGraph([('f', 'e'), ('d', 'c'), ('a', 'b'), ('c', 'd'), ('c', 'f'), ('f', 'd'), ('b', 'a'), ('a', 'd'), ('d', 'a'), ('e', 'a'), ('b', 'f'), ('a', 'c'), ('d', 'b')])
    # G = nx.DiGraph([('a', 'b'), ('b', 'c'), ('c', 'e'), ('e', 'a'), ('a', 'd'), ('d', 'c'), ('c', 'a')])
    if nx.is_eulerian(G):
        cycle = nx.eulerian_circuit(G)
        print(list(cycle))
    else:
        print("There is no Eulerian cycle in this graph")