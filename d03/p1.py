from functools import reduce
from operator import mul

print(
    reduce(
        mul,
        (
            reduce(
                f,
                map(
                    lambda l: reduce(lambda a, b: a + int(b), l, 0) > len(l) / 2,
                    zip(*map(lambda s: s[:-1], open("input.txt").readlines())),
                ),
                0,
            )
            for f in (lambda a, b: 2 * a + b, lambda a, b: 2 * a + (1 - b))
        ),
        1,
    )
)
