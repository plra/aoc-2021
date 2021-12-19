from p1 import read


def find_paths(G, start="start", end="end"):
    # Stack of pairs `(path, retread)`, where `path` is an (incomplete) path from `start` towards
    # `end` and `retread` indicates whether `path` visits the same small cave twice
    path_stack = [([start], False)]
    complete_paths = []
    while path_stack:
        path, retread = path_stack.pop()
        cur_cave = path[-1]
        if cur_cave == end:
            complete_paths.append(path)
        else:
            for nxt_cave in G[cur_cave]:
                if nxt_cave[0].isupper():
                    # We can visit large caves as much as we like
                    path_stack.append((path + [nxt_cave], retread))
                elif nxt_cave not in path:
                    # We can visit new small caves as much as we like (note start can't be new)
                    path_stack.append((path + [nxt_cave], retread))
                elif not retread and nxt_cave != start:
                    # We can visit a small cave we've already seen as long as we haven't already
                    # visited 2 small caves, and that small cave isn't start
                    path_stack.append((path + [nxt_cave], True))
    return complete_paths


if __name__ == "__main__":
    G = read("input.txt")
    print(len(find_paths(G)))
