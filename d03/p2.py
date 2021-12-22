from functools import reduce
from operator import ge, lt

print(
    reduce(
        lambda p, b: p * int(b.pop(), 2),
        (
            lambda S: reduce(
                lambda sets, i: [
                    set(
                        filter(
                            lambda s: int(s[i])
                            == (f(sum(int(s[i]) for s in sets[r]), len(sets[r]) / 2)),
                            sets[r],
                        )
                    )
                    or sets[r]
                    for r, f in [(0, ge), (1, lt)]
                ],
                range(len(S[0]) - 1),
                (set(S),) * 2,
            )
        )(open("input.txt").readlines()),
        1,
    )
)
