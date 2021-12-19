from pprint import pprint

N = 10


def read(filename):
    with open(filename) as f:
        els = []
        for line in f.readlines():
            els.append([int(d) for d in line.strip()])
    return els


def neighbors(i, j):
    nbrs = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if (di, dj) != (0, 0) and 0 <= i + di < N and 0 <= j + dj < N:
                nbrs.append((i + di, j + dj))
    return nbrs


def flash_once(els, flashers):
    for i in range(N):
        for j in range(N):
            if els[i][j] > 9 and (i, j) not in flashers:
                for i_nbr, j_nbr in neighbors(i, j):
                    els[i_nbr][j_nbr] += 1
                flashers.add((i, j))
                return True
    # No octopus flashed; signal that phase 2 is done
    return False


def step(els):
    # Increment all energy levels
    for i in range(N):
        for j in range(N):
            els[i][j] += 1

    # Repeatedly trigger flashes until octopi done
    flashers = set()
    while flash_once(els, flashers):
        pass

    # Reset energy levels of flashers
    for i, j in flashers:
        els[i][j] = 0

    return len(flashers)


if __name__ == "__main__":
    els = read("input.txt")
    print(sum(step(els) for _ in range(100)))

