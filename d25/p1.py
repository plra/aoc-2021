def read(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f.readlines()]


def step(cm):
    rows, cols = len(cm), len(cm[0])
    new_cm = [row.copy() for row in cm]
    for direction in [">", "v"]:
        for r in range(rows):
            for c in range(cols):
                if cm[r][c] != direction:
                    continue
                if direction == ">":
                    i, j = r, (c + 1) % cols
                elif direction == "v":
                    i, j = (r + 1) % rows, c
                if cm[i][j] == ".":
                    new_cm[r][c] = "."
                    new_cm[i][j] = direction
        cm = [row.copy() for row in new_cm]
    return new_cm


if __name__ == "__main__":
    cm = read("input.txt")

    for s in range(1, 2 ** 64):
        nxt = step(cm)
        if cm == nxt:
            print(s)
            break
        cm = nxt
