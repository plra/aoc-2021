from p1 import read, add

if __name__ == "__main__":
    lines = read("input.txt")
    hits = {}
    for x1, y1, x2, y2 in lines:
        add(x1, y1, x2, y2, hits)
    print(sum(n > 1 for n in hits.values()))
