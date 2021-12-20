from p1 import hits


def hit_velocities(target_area):
    _, xmax, ymin, _ = target_area
    return [
        (vx, vy)
        for vx in range(1, xmax + 1)
        for vy in range(ymin, 1000)
        if hits(vx, vy, target_area)
    ]


if __name__ == "__main__":
    target_area = (128, 160, -142, -88)
    print(len(hit_velocities(target_area)))
