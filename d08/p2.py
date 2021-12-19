from p1 import read
from itertools import permutations

DIGIT_CHARSETS = [
    set(s)
    for s in [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]
]


def mapping_works(char_mapping, coded_charsets):
    for coded_charset in coded_charsets:
        decoded_charset = {char_mapping[c] for c in coded_charset}
        if decoded_charset not in DIGIT_CHARSETS:
            return False
    return True


# Dumb brute force
def get_char_mapping(coded_charsets):
    for p in permutations("abcdefg"):
        char_mapping = dict(zip("abcdefg", p))
        if mapping_works(char_mapping, coded_charsets):
            return char_mapping


def decode(input, output):
    char_mapping = get_char_mapping(input + output)
    decoded_charsets = [
        {char_mapping[l] for l in coded_digit} for coded_digit in output
    ]
    digits = [
        DIGIT_CHARSETS.index(decoded_charset) for decoded_charset in decoded_charsets
    ]
    return int("".join(map(str, digits)))


if __name__ == "__main__":
    inputs, outputs = read("input.txt")
    print(sum(decode(input, output) for input, output in zip(inputs, outputs)))
