print(
    sum(
        xs[i] > xs[i - 1]
        for xs in [list(map(int, open("input.txt").readlines()))]
        for i in range(1, len(xs))
    )
)

