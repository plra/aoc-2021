from p1 import read, low_points


def find_basins(heights):
    lps = low_points(heights)

    rows, cols = len(heights), len(heights[0])

    basins = []
    for i_lp, j_lp in lps:
        q = [(i_lp, j_lp)]
        basin = set()
        while len(q) > 0:
            i, j = q.pop(0)
            basin.add((i, j))
            for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and heights[i][j] < heights[r][c] < 9
                    and (r, c) not in basin
                ):
                    q.append((r, c))
        basins.append(basin)
    return basins


if __name__ == "__main__":
    heights = read("input.txt")
    basins = find_basins(heights)
    sizes = sorted(map(len, basins), reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])

