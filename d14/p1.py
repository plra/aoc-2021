from collections import defaultdict as ddict


def read(filename):
    with open(filename) as f:
        template = f.readline().strip()
        f.readline()
        rules = {}
        for line in f.readlines():
            pair, elt = line.strip().split(" -> ")
            rules[pair] = elt
        return template, rules


# Naively build a string. This would be faster using a linkedlist / rope / whatever
def step(template, rules):
    # 1st char of `template` doesn't change. Consider only 2nd char of pairs to avoid duplication
    new_template = template[0]
    for i in range(len(template) - 1):
        pair = template[i : i + 2]
        # All pairs have an associated insertion rule
        new_template += rules[pair] + pair[1]
    return new_template


def substr_counts(s, substr_length=1):
    counts = ddict(lambda: 0)
    for i in range(len(s) - substr_length + 1):
        substr = s[i : i + substr_length]
        counts[substr] += 1
    return counts


if __name__ == "__main__":
    template, rules = read("input.txt")
    for _ in range(10):
        template = step(template, rules)
    char_counts = substr_counts(template)
    print(max(char_counts.values()) - min(char_counts.values()))
