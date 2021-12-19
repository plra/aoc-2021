from p1 import read, substr_counts, ddict


# Order only matters up to substrings of length 2. Hence work with dict of pair counts
def step(pair_counts, char_counts, rules):
    new_char_counts = char_counts.copy()
    new_pair_counts = ddict(lambda: 0)
    for pair, n in pair_counts.items():
        # A `new_char` `x` is inserted between each `pair` `ab`. We get `n` new occurrences of `x`,
        # as well as of `ax` and `xb`.
        new_char = rules[pair]
        new_char_counts[rules[pair]] += n
        new_pair_counts[pair[0] + new_char] += n
        new_pair_counts[new_char + pair[1]] += n
    return new_pair_counts, new_char_counts


if __name__ == "__main__":
    template, rules = read("input.txt")
    pair_counts = substr_counts(template, 2)
    char_counts = substr_counts(template)
    for _ in range(40):
        pair_counts, char_counts = step(pair_counts, char_counts, rules)
    print(max(char_counts.values()) - min(char_counts.values()))
