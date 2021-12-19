def read(filename):
    dots = set()
    folds = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            elif line.startswith("fold"):
                instr, coord = line.split("=")
                folds.append((instr[-1], int(coord)))
            else:
                x, y = map(int, line.split(","))
                dots.add((x, y))
    return dots, folds


def fold(dots, axis, coord):
    new_dots = set()
    if axis == "x":
        for x, y in dots:
            if x < coord:
                new_dots.add((x, y))
            else:
                new_x = coord - (x - coord)
                new_dots.add((new_x, y))
    elif axis == "y":
        for x, y in dots:
            if y < coord:
                new_dots.add((x, y))
            else:
                new_y = coord - (y - coord)
                new_dots.add((x, new_y))
    return new_dots


if __name__ == "__main__":
    dots, folds = read("input.txt")
    axis, coord = folds[0]
    print(len(fold(dots, axis, coord)))
