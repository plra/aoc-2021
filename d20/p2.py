from p1 import *

if __name__ == "__main__":
    iea, im = read("input.txt")

    print(n_lit(enhance_times(im, iea, 50)))

