with open("input_0.txt") as f:
    depths = [int(line.strip()) for line in f.readlines()]
    print(sum(depths[i] > depths[i - 1] for i in range(1, len(depths))))

