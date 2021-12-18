def read(filename):
    with open(filename) as f:
        return list(map(int, f.readline().strip().split(",")))


def step(ages):
    for i in range(len(ages)):
        if ages[i] > 0:
            ages[i] -= 1
        else:
            ages[i] = 6
            ages.append(8)


if __name__ == "__main__":
    ages = read("input.txt")
    for _ in range(80):
        step(ages)
    print(len(ages))
