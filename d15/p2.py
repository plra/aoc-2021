from p1 import read, robp


def augment(risk, N=5):
    rows, cols = len(risk), len(risk[0])
    new_risk = [[None for _ in range(N * cols)] for _ in range(N * rows)]
    for I in range(N):
        for J in range(N):
            for i in range(rows):
                for j in range(cols):
                    new_risk[I * rows + i][J * rows + j] = (risk[i][j] + I + J) % 9 or 9
    return new_risk


if __name__ == "__main__":
    risk = read("input.txt")
    print(robp(augment(risk)))
