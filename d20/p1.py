from itertools import product


def read(filename):
    with open(filename) as f:
        iea = f.readline().strip()
        f.readline()
        im = []
        for line in f.readlines():
            im.append(list(line.strip()))
        return iea, im


def show(im):
    for row in im:
        print("".join(row))
    print()


def get_px(im, iea, i, j, surroundings="."):
    rows, cols = len(im), len(im[0])
    nbrs = product(range(i - 1, i + 2), range(j - 1, j + 2))
    idx_binary = ""
    for r, c in nbrs:
        px = im[r][c] if 0 <= r < rows and 0 <= c < cols else surroundings
        idx_binary += "1" if px == "#" else "0"
    idx = int(idx_binary, 2)
    return iea[idx]


def pad(im, n=1, px="."):
    rows, _ = len(im), len(im[0])
    new_im = []
    new_im += [[px] * (n + rows + n)] * n
    for row in im:
        new_im.append([px] * n + row + [px] * n)
    new_im += [[px] * (n + rows + n)] * n
    return new_im


def enhance(im, iea, surroundings="."):
    im = pad(im, px=surroundings)
    new_im = [row.copy() for row in im]
    rows, cols = len(new_im), len(new_im[0])
    for i in range(rows):
        for j in range(cols):
            new_im[i][j] = get_px(im, iea, i, j, surroundings)
    return new_im


def enhance_times(im, iea, n):
    for i in range(n):
        if iea[0] == "." or i % 2 == 0:
            surroundings = "."
        else:
            surroundings = "#"
        im = enhance(im, iea, surroundings)
    return im


def n_lit(im):
    return sum(px == "#" for row in im for px in row)


if __name__ == "__main__":
    iea, im = read("input.txt")

    print(n_lit(enhance_times(im, iea, 2)))

