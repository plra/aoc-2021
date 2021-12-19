from statistics import median


def read(filename):
    with open(filename) as f:
        return list(map(int, f.readline().strip().split(",")))


# The median minimizes L1 loss:
# \argmin_m \sum_{i=1}^n |X_i - m| = med(X_1, ..., X_n).
def solve(positions):
    med = median(positions)
    return sum(abs(pos - med) for pos in positions)


if __name__ == "__main__":
    positions = read("input.txt")
    print(solve(positions))

