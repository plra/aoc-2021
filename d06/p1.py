def read(filename):
    with open(filename) as f:
        age_list = map(int, f.readline().strip().split(","))
        age_counts = {age: 0 for age in range(9)}
        for age in age_list:
            age_counts[age] += 1
        return age_counts


# Lame iterative solution. This can be done mathematically
def step(age_counts):
    new_counts = {age: 0 for age in range(9)}
    for age, count in age_counts.items():
        if age == 0:
            new_counts[6] += count
            new_counts[8] += count
        else:
            new_counts[age - 1] += count
    return new_counts


def solve(age_counts, days):
    for _ in range(days):
        age_counts = step(age_counts)
    return sum(age_counts.values())


if __name__ == "__main__":
    age_counts = read("input.txt")
    print(solve(age_counts, 80))
