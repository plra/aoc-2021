import re


def read(filename):
    steps = []
    with open(filename) as f:
        for line in f.readlines():
            instr = line[:3].strip()
            xa, xb, ya, yb, za, zb = [int(t) for t in re.split(r"[^-\d]+", line) if t]
            steps.append((instr, ((xa, xb), (ya, yb), (za, zb))))
    return steps


if __name__ == "__main__":
    steps = read("input.txt")

    # Naive pointset
    cubes_on = set()
    for instr, cuboid in steps:
        if any(abs(t) > 50 for i in cuboid for t in i):
            continue
        (xa, xb), (ya, yb), (za, zb) = cuboid
        for x in range(xa, xb + 1):
            for y in range(ya, yb + 1):
                for z in range(za, zb + 1):
                    if instr == "on":
                        cubes_on.add((x, y, z))
                    else:
                        cubes_on.discard((x, y, z))

    print(len(cubes_on))
