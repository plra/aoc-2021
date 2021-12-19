WIDTH = 5


def read(filename):
    with open(filename) as f:
        draws = list(map(int, f.readline().split(",")))
        boards = []
        while f.readline():
            board = []
            for _ in range(WIDTH):
                row_vals = map(int, f.readline().split())
                board.append(list(zip(row_vals, [False for _ in range(WIDTH)])))
            boards.append(board)
        return draws, boards


def mark(board, draw):
    for i in range(WIDTH):
        for j in range(WIDTH):
            num, _ = board[i][j]
            if num == draw:
                board[i][j] = (num, True)


def wins_by_row(board):
    return any(all(found for n, found in row) for row in board)


def wins(board):
    board_t = list(map(list, zip(*board)))
    return wins_by_row(board) or wins_by_row(board_t)


def score(board, draw):
    return draw * sum(n for row in board for n, found in row if not found)


if __name__ == "__main__":
    draws, boards = read("input.txt")
    done = False
    for draw in draws:
        for board in boards:
            mark(board, draw)
            if wins(board):
                done = True
                break
        if done:
            print(score(board, draw))
            break
