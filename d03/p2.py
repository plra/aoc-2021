from functools import reduce
from operator import ge, lt

print(
    reduce(
        lambda x, y: x * int(y.pop(), 2),
        [
            reduce(
                lambda sets, i: [
                    {
                        s
                        for s in sets[r]
                        if int(s[i])
                        == (f(sum(int(s[i]) for s in sets[r]), len(sets[r]) / 2))
                    }
                    or sets[r]
                    for r, f in [(0, ge), (1, lt)]
                ],
                range(len(S[0]) - 1),
                (set(S),) * 2,
            )
            for S in [open("input.txt").readlines()]
        ].pop(),
        1,
    )
)
