from functools import reduce
from operator import mul

bitstrings = None
with open("input.txt") as f:
    bitstrings = [b.strip() for b in f.readlines()]

n, k = len(bitstrings), len(bitstrings[0])
o2, co2 = set(bitstrings), set(bitstrings)

for bit in range(k):
    o2_ones = sum(int(bitstring[bit]) for bitstring in o2)
    co2_ones = sum(int(bitstring[bit]) for bitstring in co2)
    o2_bit = int(o2_ones >= len(o2) / 2)
    co2_bit = int(co2_ones < len(co2) / 2)

    if len(o2) > 1:
        o2 = {bs for bs in o2 if int(bs[bit]) == o2_bit}
    if len(co2) > 1:
        co2 = {bs for bs in co2 if int(bs[bit]) == co2_bit}
    print(f"pos {bit}: (o2, co2)=({o2_bit}, {co2_bit}), ({len(o2)}, {len(co2)})")

print(o2, co2)
print(int(o2.pop(), 2) * int(co2.pop(), 2))
