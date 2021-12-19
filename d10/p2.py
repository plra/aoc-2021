from p1 import read, L, R, L2R
from statistics import median


def completion(line):
    stack = []
    for sym in line:
        if sym in L:
            stack.append(sym)
        elif sym in R:
            prv_sym = stack.pop()
            if not (prv_sym in L and L2R[prv_sym] == sym):
                # Corrupted
                return []
    return [L2R[sym] for sym in stack[::-1]]


POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def score(completion):
    s = 0
    for sym in completion:
        s = 5 * s + POINTS[sym]
    return s


if __name__ == "__main__":
    lines = read("input.txt")
    scores = [score(completion(line)) for line in lines if completion(line)]
    print(median(scores))
