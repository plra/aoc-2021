import re


def read(filename):
    lines = []
    with open(filename) as f:
        for line in f.readlines():
            x1, y1, x2, y2 = map(int, re.split(r"\D+", line.strip()))
            lines.append((x1, y1, x2, y2))
    return lines


def add(x1, y1, x2, y2, hits):
    x_incr = (x2 > x1) - (x2 < x1)
    y_incr = (y2 > y1) - (y2 < y1)

    x, y = x1, y1
    while True:
        if (x, y) not in hits:
            hits[(x, y)] = 1
        else:
            hits[(x, y)] += 1

        if (x, y) == (x2, y2):
            break
        x += x_incr
        y += y_incr


if __name__ == "__main__":
    lines = read("input.txt")
    hits = {}
    for x1, y1, x2, y2 in lines:
        if x1 == x2 or y1 == y2:
            add(x1, y1, x2, y2, hits)
    print(sum(n > 1 for n in hits.values()))
