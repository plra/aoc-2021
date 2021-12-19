def read(filename):
    heights = []
    with open(filename) as f:
        for line in f.readlines():
            heights.append([int(d) for d in line.strip()])
    return heights


def low_points(heights):
    rows = len(heights)
    cols = len(heights[0])
    lps = []
    for i in range(rows):
        for j in range(cols):
            if all(
                heights[i][j] < heights[r][c]
                for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                if 0 <= r < rows and 0 <= c < cols
            ):
                lps.append((i, j))
    return lps


def solve(heights):
    lps = low_points(heights)
    return sum(heights[i][j] + 1 for i, j in lps)


if __name__ == "__main__":
    heights = read("input.txt")
    print(solve(heights))
