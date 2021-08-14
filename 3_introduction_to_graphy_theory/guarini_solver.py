import networkx as nx
import itertools as it

def add_all_config(G: nx.Graph) -> None:
    for wb_indices in it.permutations(range(8), r=4):
        config = ['*'] * 8
        config[wb_indices[0]] = 'W'
        config[wb_indices[1]] = 'W'
        config[wb_indices[2]] = 'B'
        config[wb_indices[3]] = 'B'

        G.add_node(''.join(config))

def get_all_moves() -> list:
    moves = [[] for _ in range(8)]
    # possible movements in all eight positions
    moves[0] = [4, 6]
    moves[1] = [5, 7]
    moves[2] = [3, 6]
    moves[3] = [2, 7]
    moves[4] = [0, 5]
    moves[5] = [1, 4]
    moves[6] = [0, 2]
    moves[7] = [1, 3]
    return moves

def add_all_edges(G: nx.Graph, moves: list) -> None:
    # check every configuration (vertex)
    for node in G.nodes():
        config = [c for c in node]
        # check if there is a valid move to another configuration in all 8 positions
        for i in range(8):
            if config[i] == '*':
                continue
            for new_pos in moves[i]:
                if config[new_pos] != '*':
                    continue
                new_config = config.copy()
                new_config[i] = '*'
                new_config[new_pos] = config[i]
                # add new edge
                if not G.has_edge(''.join(config), ''.join(new_config)):
                    G.add_edge(''.join(config), ''.join(new_config))

if __name__ == "__main__":
    G = nx.Graph()
    add_all_config(G) # add all vertices
    moves = get_all_moves()
    add_all_edges(G, moves)
    # check if two board configurations are reachable to each other
    assert "W*B**W*B" in nx.node_connected_component(G, "W*W**B*B")
    assert "B*B**W*W" in nx.node_connected_component(G, "W*W**B*B")
    assert "W*B**B*W" not in nx.node_connected_component(G, "W*W**B*B")
    # display shortest path
    print(" -> ".join(nx.shortest_path(G, "W*W**B*B", "B*B**W*W")))