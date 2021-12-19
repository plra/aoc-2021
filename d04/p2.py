from pprint import pprint
from p1 import WIDTH, read, mark, wins, score

draws, boards = read("input.txt")
already_won = [False for _ in range(len(boards))]

last_winning_score = None
for draw in draws:
    for i, board in enumerate(boards):
        mark(board, draw)
        if wins(board) and not already_won[i]:
            last_winning_score = score(board, draw)
            already_won[i] = True
            print(f"Win on board {i+1} for draw {draw}: score {last_winning_score}")


print(last_winning_score)
