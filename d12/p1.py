import networkx as nx


def read(filename):
    G = nx.Graph()
    with open(filename) as f:
        for line in f.readlines():
            u, v = line.strip().split("-")
            G.add_edge(u, v)
    return G


# Do it manually with a stack
def find_paths(G, start="start", end="end"):
    path_stack = [[start]]
    complete_paths = []
    while path_stack:
        cur_path = path_stack.pop()
        cur_cave = cur_path[-1]
        if cur_cave == end:
            complete_paths.append(cur_path)
        else:
            for nxt_cave in G[cur_cave]:
                if nxt_cave[0].isupper() or nxt_cave not in cur_path:
                    # We can visit a cave only if it's large or unseen
                    path_stack.append(cur_path + [nxt_cave])
    return complete_paths


if __name__ == "__main__":
    G = read("input.txt")
    print(len(find_paths(G)))
