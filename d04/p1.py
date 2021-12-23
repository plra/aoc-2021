from functools import reduce

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


lmap = lambda f, xs: list(map(f, xs))


print(
    (
        lambda draws, boards: reduce(
            lambda result_and_boards, draw: (
                (
                    lambda boards: (
                        reduce(
                            lambda score, board: sum(
                                n for row in board for (n, seen) in row if not seen
                            )
                            * draw
                            if score is None
                            and any(
                                all(seen for (_, seen) in row)
                                for b in [board, zip(*board)]
                                for row in b
                            )
                            else score,
                            boards,
                            None,
                        ),
                        boards,
                    )
                )(
                    lmap(
                        lambda board: lmap(
                            lambda row: lmap(
                                lambda e: (e[0], draw == e[0] or e[1]), row
                            ),
                            board,
                        ),
                        result_and_boards[1],
                    )
                )
                if result_and_boards[0] is None
                else result_and_boards
            ),
            draws,
            (None, boards),
        )[0]
    )(*read("input.txt"))
)
