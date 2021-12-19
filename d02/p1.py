from functools import reduce
from operator import mul

print(
    reduce(
        mul,
        (
            f([l.strip().split() for l in open("input.txt").readlines()])
            for f in [
                lambda cs: sum(int(x) for d, x in cs if d[0] == "f"),
                lambda cs: sum(
                    int(x) * (-1) ** (d[0] == "u") for d, x in cs if d[0] != "f"
                ),
            ]
        ),
        1,
    )
)
