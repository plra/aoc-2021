from p1 import read

# Now the cost of moving n steps is n(n+1)/2 \propto n^2 + n. Mean minimizes the quadratic term,
# but I'm not sure if there's a simple statistic which minimizes this "ridge" loss.
# Disappointingly, this works:
def solve(positions):
    best_cost = 2 ** 64
    for ctr in range(min(positions), max(positions) + 1):
        ns = [abs(pos - ctr) for pos in positions]
        cost = sum(n * (n + 1) / 2 for n in ns)
        if cost < best_cost:
            best_cost = cost
    return best_cost


if __name__ == "__main__":
    positions = read("input.txt")
    print(solve(positions))
