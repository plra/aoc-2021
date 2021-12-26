# Time to beat: python3 p1.py  13.02s user 0.51s system 96% cpu 13.977 total

import networkx as nx
from networkx.algorithms import shortest_path_length
from copy import deepcopy

ENERGY_PER_MOVE = {"A": 1, "B": 10, "C": 100, "D": 1000}
DESTINATION_COLS = {"A": 2, "B": 4, "C": 6, "D": 8}

START_BURROW_STRING = "...........\n##D#C#D#B##\n #C#A#A#B# "
END_BURROW_STRING = "...........\n##A#B#C#D##\n #A#B#C#D# "


def parse(diagram):
    return [list(line) for line in diagram.split("\n")]


def to_string(burrow):
    return "\n".join(["".join(row) for row in burrow])


# 0  ...........  hall
# 1  ##A#B#C#D##  2
# 2   #A#B#C#D#
# 3   #A#B#C#D#
# 4   #A#B#C#D#    r_lowest
#    0 2 4 6 8 t
#       ^ ^ ^ ^
#        rooms

# Get moves for pod at position (r, c) as (r_dest, c_dest, hops)
def possible_moves_from(r, c, burrow):
    pod = burrow[r][c]

    hall_row = 0
    hall = burrow[hall_row]
    hall_left_col, hall_right_col = 0, 10
    room_top_row = 1
    room_bottom_row = len(burrow) - 1

    if r > hall_row:  # Move from a room to the hall
        # Can't move if other pod is blocking room exit. This will only happen if there's
        # a pod immediately above.
        if r > room_top_row and burrow[r - 1][c] != ".":
            return []

        # Don't move if pod is already at a valid destination position
        if c == DESTINATION_COLS[pod] and all(
            burrow[r_room][c] in [".", pod] for r_room in range(1, room_bottom_row + 1)
        ):
            return []

        # TODO: Force direct room-to-room moves when available.

        # Add a move for each position we can reach in the left or right
        # subhall without hitting something
        moves = []

        for subhall in [
            list(range(c - 1, hall_left_col, -2)) + [hall_left_col],
            list(range(c + 1, hall_right_col, 2)) + [hall_right_col],
        ]:
            for c_hall in subhall:
                if hall[c_hall] != ".":
                    break
                moves.append((hall_row, c_hall, abs(c_hall - c) + r))

        return moves
    else:  # Move from the hall to a room
        c_dest = DESTINATION_COLS[pod]

        # Check if room is enterable
        if any(
            burrow[r_room][c_dest] not in [".", pod]
            for r_room in range(room_top_row, room_bottom_row + 1)
        ):
            return []

        # Check if hallway is clear
        if c < c_dest:
            subhall = range(max(c, hall_left_col + 1), c_dest, 2)
        else:
            subhall = range(min(c, hall_right_col - 1), c_dest, -2)

        if all(hall[c_hall] == "." or c_hall == c for c_hall in subhall):
            # Go as far down in room as possible
            for r_dest in range(room_bottom_row, room_top_row - 1, -1):
                if burrow[r_dest][c_dest] == ".":
                    return [(r_dest, c_dest, abs(c_dest - c) + r_dest)]

        # We don't need to consider hall-to-hall moves.
        return []


# Get all moves for pods in burrow as [(pod, r, c, r_dest, c_dest, hops)]
def possible_moves(burrow):
    moves = []
    for r in range(len(burrow)):
        for c in range(len(burrow[0])):
            if burrow[r][c] in "ABCD":
                pod_moves = possible_moves_from(r, c, burrow)
                moves.extend([(burrow[r][c], r, c, *move) for move in pod_moves])
    return moves


def update(burrow, move):
    pod, r, c, r_dest, c_dest, _ = move
    burrow[r][c] = "."
    burrow[r_dest][c_dest] = pod


def energy(move):
    pod, _, _, _, _, hops = move
    return ENERGY_PER_MOVE[pod] * hops


# Build state graph with string representations of reachable burrow configurations as nodes,
# and edges uv with weight e if configuration v can be reached from u by moving one pod,
# where e is the energy spent by moving the pod.
def build_burrow_graph(initial_burrow):
    G = nx.DiGraph()
    unseen_burrows = [initial_burrow]
    while unseen_burrows:
        burrow = unseen_burrows.pop()
        burrow_string = to_string(burrow)
        G.add_node(burrow_string)

        for move in possible_moves(burrow):
            new_burrow = deepcopy(burrow)
            update(new_burrow, move)
            new_burrow_string = to_string(new_burrow)

            if new_burrow_string not in G.nodes:
                G.add_node(new_burrow_string)
                unseen_burrows.append(new_burrow)
            G.add_edge(burrow_string, new_burrow_string, weight=energy(move))
    return G


if __name__ == "__main__":
    start_burrow = parse(START_BURROW_STRING)
    G = build_burrow_graph(start_burrow)
    # Find lowest-energy solution by running Dijkstra on G
    print(
        shortest_path_length(G, START_BURROW_STRING, END_BURROW_STRING, weight="weight")
    )
