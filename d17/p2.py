from p1 import hits, min_vx


def hit_velocities(target_area):
    xmin, xmax, ymin, _ = target_area
    hvs = []
    for vx in range(min_vx(xmin), xmax + 1):
        for vy in range(ymin, 1000):
            if hits(vx, vy, target_area):
                hvs.append((vx, vy))
    return hvs


if __name__ == "__main__":
    target_area = (128, 160, -142, -88)
    print(len(hit_velocities(target_area)))
