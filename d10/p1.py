def read(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


L = ["(", "[", "{", "<"]
R = [")", "]", "}", ">"]
L2R = dict(zip(L, R))
POINTS = dict(zip(R, [3, 57, 1197, 25137]))


def syntax_error_score(line):
    stack = []
    for sym in line:
        if sym in L:
            stack.append(sym)
        elif sym in R:
            prv_sym = stack.pop()
            if not (prv_sym in L and L2R[prv_sym] == sym):
                return POINTS[sym]
    return 0


if __name__ == "__main__":
    lines = read("input.txt")
    print(sum(syntax_error_score(line) for line in lines))
