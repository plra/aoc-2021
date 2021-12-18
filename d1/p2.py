with open("input.txt") as f:
    depths = [int(line.strip()) for line in f.readlines()]

    n_increases = 0
    for i in range(3, len(depths)):
        cur_sum = depths[i] + depths[i - 1] + depths[i - 2]
        prv_sum = depths[i - 1] + depths[i - 2] + depths[i - 3]
        n_increases += cur_sum > prv_sum

    print(n_increases)
