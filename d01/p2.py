print(
    sum(
        xs[i] > xs[i - 3]
        for xs in [list(map(int, open("input.txt").readlines()))]
        for i in range(3, len(xs))
    )
)

