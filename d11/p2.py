from p1 import read, step, N


if __name__ == "__main__":
    els = read("input.txt")
    for s in range(1, 2 ** 64):
        step(els)
        if all(els[i][j] == 0 for i in range(N) for j in range(N)):
            print(s)
            break
