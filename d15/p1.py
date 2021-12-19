import networkx as nx


def read(filename):
    risk = []
    with open(filename) as f:
        for line in f.readlines():
            risk.append(list(map(int, line.strip())))
    return risk


# We can move in directions other than right/down so DP matrix solution seems infeasible.
# Build a graph and do shortest path instead. I'm not rewriting Dijkstra
def robp(risk):
    rows, cols = len(risk), len(risk[0])
    G = nx.DiGraph()
    for i in range(rows):
        for j in range(cols):
            for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= r < rows and 0 <= c < cols:
                    G.add_edge((i, j), (r, c), weight=risk[r][c])
    return nx.shortest_path_length(
        G, source=(0, 0), target=(rows - 1, cols - 1), weight="weight"
    )


if __name__ == "__main__":
    risk = read("input.txt")
    print(robp(risk))
