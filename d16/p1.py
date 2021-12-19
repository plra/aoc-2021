from functools import reduce


def read(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines() if not line.startswith("#")]


# Evaluation functionality added after submission of p1
def parse(bn):
    version = int(bn[:3], 2)
    type_id = int(bn[3:6], 2)
    length = 6
    val = None
    subpackets = None
    vsum = version

    if type_id == 4:  # Literal
        val_bn = ""
        for i in range(6, len(bn), 5):
            val_bn += bn[i + 1 : i + 5]
            length += 5
            if bn[i] == "0":
                break
        val = int(val_bn, 2)

    else:  # Operator
        length_type_id = bn[6]
        length += 1

        # Parse subpackets
        if length_type_id == "0":  # Total length of subpackets specified
            subpackets_len = int(bn[7:22], 2)
            length += 15
            subpackets_bin = bn[22 : 22 + subpackets_len]
            length += subpackets_len
            subpackets = []
            while subpackets_bin:
                subpacket = parse(subpackets_bin)
                subpackets.append(subpacket)
                vsum += subpacket["vsum"]
                subpackets_bin = subpackets_bin[subpacket["len"] :]
        elif length_type_id == "1":  # Number of subpackets specified
            n_subpackets = int(bn[7:18], 2)
            length += 11
            subpackets_bin = bn[18:]
            subpackets = []
            for _ in range(n_subpackets):
                subpacket = parse(subpackets_bin)
                subpackets.append(subpacket)
                vsum += subpacket["vsum"]
                subpackets_bin = subpackets_bin[subpacket["len"] :]
                length += subpacket["len"]

        # Apply operation
        args = [sp["val"] for sp in subpackets]
        if type_id == 0:  # Sum
            val = reduce(lambda x, y: x + y, args, 0)
        elif type_id == 1:  # Product
            val = reduce(lambda x, y: x * y, args, 1)
        elif type_id == 2:  # Min
            val = reduce(lambda x, y: min(x, y), args, 2 ** 64)
        elif type_id == 3:  # Max
            val = reduce(lambda x, y: max(x, y), args, -2 ** 64)
        elif type_id == 5:  # >
            val = int(args[0] > args[1])
        elif type_id == 6:  # <
            val = int(args[0] < args[1])
        elif type_id == 7:  # ==
            val = int(args[0] == args[1])

    return {
        "ver": version,
        "len": length,
        "val": val,
        "subpackets": subpackets,
        "vsum": vsum,
    }


if __name__ == "__main__":
    hex_inputs = read("input.txt")
    for hex_input in hex_inputs:
        bin_input = bin(int(hex_input, 16))[2:].zfill(len(hex_input) * 4)
        print(parse(bin_input)["vsum"])
