def read(filename):
    patterns = []
    outputs = []
    with open(filename) as f:
        for line in f.readlines():
            pattern_strs, output_strs = line.strip().split(" | ")
            patterns.append(pattern_strs.split())
            outputs.append(output_strs.split())
    return patterns, outputs


def count_1478s(outputs):
    return sum(len(digit) in [2, 3, 4, 7] for output in outputs for digit in output)


if __name__ == "__main__":
    patterns, outputs = read("input.txt")
    print(patterns, outputs)
    print(count_1478s(outputs))
