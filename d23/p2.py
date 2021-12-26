from p1 import build_burrow_graph, parse
from networkx.algorithms import shortest_path_length

START_BURROW_STRING = "...........\n##D#C#D#B##\n #D#C#B#A# \n #D#B#A#C# \n #C#A#A#B# "
END_BURROW_STRING = "...........\n##A#B#C#D##\n #A#B#C#D# \n #A#B#C#D# \n #A#B#C#D# "

if __name__ == "__main__":
    start_burrow = parse(START_BURROW_STRING)
    G = build_burrow_graph(start_burrow)
    print(
        shortest_path_length(G, START_BURROW_STRING, END_BURROW_STRING, weight="weight")
    )
