from p1 import read
from functools import reduce, lru_cache
from operator import mul


def interval_overlap(i, j):
    (i, j) = (i, j) if i <= j else (j, i)
    return (j[0], min(i[1], j[1])) if i[1] >= j[0] else None


@lru_cache(maxsize=None)
def cuboid_overlap(cuboid, new_cuboid):
    ol = tuple(interval_overlap(cuboid[i], new_cuboid[i]) for i in range(len(cuboid)))
    return ol if None not in ol else None


def volume(cuboid):
    return reduce(mul, (b - a + 1 for a, b in cuboid), 1)


# Determine change in number of "on" cubes and extra steps associated with new instruction/cuboid.
# If new cuboid doesn't overlap with any past cuboids, just add it.
# For each cuboid in prv_steps the new cuboid overlaps with, add a step to new_steps that undoes
# the double-counting associated with adding/removing volumes of overlapping cuboids.
def step(prv_steps, new_instr, new_cuboid):
    new_cubes, new_steps = 0, []
    for instr, cuboid in prv_steps:
        overlap = cuboid_overlap(cuboid, new_cuboid)
        if overlap and instr == "on":
            new_steps.append(("off", overlap))
            new_cubes -= volume(overlap)
        elif overlap and instr == "off":
            new_steps.append(("on", overlap))
            new_cubes += volume(overlap)

    if new_instr == "on":
        new_cubes += volume(new_cuboid)
        new_steps.append(("on", new_cuboid))

    return new_cubes, new_steps


if __name__ == "__main__":
    steps = read("input.txt")
    prv_steps = []
    n_on = 0
    for new_instr, new_cuboid in steps:
        new_cubes, new_steps = step(prv_steps, new_instr, new_cuboid)
        prv_steps += new_steps
        n_on += new_cubes
    print(n_on)
