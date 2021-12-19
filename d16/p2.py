from p1 import read, parse


if __name__ == "__main__":
    hex_inputs = read("input.txt")
    for hex_input in hex_inputs:
        bin_input = bin(int(hex_input, 16))[2:].zfill(len(hex_input) * 4)
        print(parse(bin_input)["val"])
