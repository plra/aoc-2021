from p1 import read


def find_paths(G, start="start", end="end"):
    # Stack containing pairs (incomplete) paths from start towards end along with an indicator of
    # whether that path contains 2 visits of the same small cave
    path_stack = [([start], False)]
    complete_paths = []
    while path_stack:
        cur_path, visited_2_small_caves = path_stack.pop()
        cur_cave = cur_path[-1]
        if cur_cave == end:
            complete_paths.append(cur_path)
        else:
            for nxt_cave in G[cur_cave]:
                if nxt_cave[0].isupper():
                    # We can visit large caves as much as we like
                    path_stack.append((cur_path + [nxt_cave], visited_2_small_caves))
                elif nxt_cave not in cur_path:
                    # We can visit new small caves as much as we like (note start can't be new)
                    path_stack.append((cur_path + [nxt_cave], visited_2_small_caves))
                elif not visited_2_small_caves and nxt_cave != start:
                    # We can visit a small cave we've already seen as long as we haven't already
                    # visited 2 small caves, and that small cave isn't start
                    path_stack.append((cur_path + [nxt_cave], True))
    return complete_paths


if __name__ == "__main__":
    G = read("input.txt")
    print(len(find_paths(G)))
