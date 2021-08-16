import networkx as nx

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        ('a', 'b', {'weight':2, 'label': 2}), 
        ('a', 'c', {'weight':3, 'label': 3}), 
        ('a', 'd', {'weight':1, 'label': 1}), 
        ('a', 'e', {'weight':3, 'label': 3}), 
        ('b', 'c', {'weight':4, 'label': 4}), 
        ('c', 'd', {'weight':5, 'label': 5}), 
        ('d', 'e', {'weight':4, 'label': 4}), 
        ('e', 'a', {'weight':1, 'label': 1})
    ])
    T = nx.minimum_spanning_tree(G)
    for e in T.edges():
        print(e)