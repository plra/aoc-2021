from functools import reduce


print(
    reduce(
        lambda x, y: x * y[0] * y[1],
        [
            reduce(
                lambda x, y: (x[0] + int(y[1]), x[1] + x[2] * int(y[1]), x[2])
                if y[0][0] == "f"
                else (x[0], x[1], x[2] + (-1) ** (y[0] == "up") * int(y[1])),
                map(lambda s: s.strip().split(), open("input.txt").readlines()),
                (0, 0, 0),
            )
        ],
        1,
    )
)

