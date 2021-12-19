from p1 import read, fold
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dots, folds = read("input.txt")
    for axis, coord in folds:
        dots = fold(dots, axis, coord)
    print(dots)
    xs, ys = list(zip(*dots))
    plt.figure(figsize=(20, 2))
    plt.scatter(xs, [-y for y in ys])
    plt.show()
