from math import sqrt

PRECISION = 5


def read(filename):
    scanners = []
    with open(filename) as f:
        for line in f.readlines():
            if line.startswith("---"):
                coords = []
            elif line == "\n":
                scanners.append(coords)
            else:
                x, y, z = map(int, line.strip().split(","))
                coords.append((x, y, z))
        scanners.append(coords)
    return scanners


# Build dict giving pairwise distances between `coords`, up to `PRECISION` digits.
def dist_map(coords):
    ds = {}
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            xi, yi, zi = coords[i]
            xj, yj, zj = coords[j]
            d = sqrt((xj - xi) ** 2 + (yj - yi) ** 2 + (zj - zi) ** 2)
            ds[(i, j)] = round(d, PRECISION)
    return ds


# Build list of "2-sets" `[((r, i_r), (r, j_r), (s, i_s), (s, j_s)), ...]` where each entry means
# `{b(r, i_r), b(r, j_r)} == {b(s, i_s), b(s, j_s)}`, where `r`, `s` are scanner indices,
# `i_r`, is a beacon index for scanner `r`, etc., and `b(r, i_r)` is the beacon seen by
# scanner `r` at index `i_r`.
def find_equal_2sets(dist_maps):
    e2s = []
    # Iterate over distinct pairs of scanners
    for r in range(len(dist_maps)):
        for s in range(r + 1, len(dist_maps)):
            # Iterate over pairs of coordinates of beacons as specified by scanners `r`, `s`
            for (i_r, j_r), d_r in dist_maps[r].items():
                for (i_s, j_s), d_s in dist_maps[s].items():
                    # Take scanners to be identical if their distances are equal
                    if d_r == d_s:
                        e2s.append(((r, i_r), (r, j_r), (s, i_s), (s, j_s)))
    return e2s


def add_equivalence(equiv_classes, x, y):
    for ec in equiv_classes:
        if x in ec:
            ec.add(y)
            return
        elif y in ec:
            ec.add(x)
            return
    equiv_classes.append({x, y})


# Given a list of equal 2-sets `[{a, b} == {c, d}]`, partition entries into equivalence classes
# by finding pairs of relations such as `({a, b} == {c, d}, {a, f} == {c, h})`, from which we
# can conclude `a == c, b == d, f == h`, and so on for other orderings.
def find_equiv_classes(equal_2sets):
    equiv_classes = []
    for i in range(len(equal_2sets)):
        for j in range(i + 1, len(equal_2sets)):
            a, b, c, d = equal_2sets[i]
            e, f, g, h = equal_2sets[j]

            pairs = []
            if (a, c) == (e, g):
                pairs = [(a, c), (b, d), (f, h)]
            elif (a, d) == (e, h):
                pairs = [(a, d), (b, c), (f, g)]
            elif (b, c) == (f, g):
                pairs = [(b, c), (a, d), (e, h)]
            elif (b, d) == (f, h):
                pairs = [(b, d), (a, c), (e, g)]

            for x, y in pairs:
                add_equivalence(equiv_classes, x, y)

    return equiv_classes


# Get beacons with exactly one index `(r, i)`, i.e. which are seen by only one scanner and hence
# do not appear in equivalence classes.
def find_lonely_beacons(scanners, equiv_classes):
    matched_beacons = set()
    for ec in equiv_classes:
        matched_beacons |= ec

    lbs = []
    for r in range(len(scanners)):
        for i in range(len(scanners[r])):
            if (r, i) not in matched_beacons:
                lbs.append((r, i))
    return lbs


if __name__ == "__main__":
    scanners = read("input.txt")
    dist_maps = [dist_map(coords) for coords in scanners]
    equal_2sets = find_equal_2sets(dist_maps)
    equiv_classes = find_equiv_classes(equal_2sets)
    lonely_beacons = find_lonely_beacons(scanners, equiv_classes)
    n_beacons = len(equiv_classes) + len(lonely_beacons)

    print(n_beacons)
