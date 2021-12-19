with open("input.txt") as f:
    horz, depth, aim = 0, 0, 0
    for line in f.readlines():
        dir, x = line.strip().split()
        x = int(x)

        if dir == "down":
            aim += x
        elif dir == "up":
            aim -= x
        elif dir == "forward":
            horz += x
            depth += aim * x

    print(horz * depth)
