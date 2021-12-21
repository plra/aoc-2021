from math import sqrt, floor, ceil


# We have `y(t) = (vy_0 + 1/2)t - t^2/2`. Setting `ymin <= y(t) <= ymax` gives us bounds on `t`
# if/when the probe is in the target area. Use quadratic formula. Same for `x`
def t_range(vy_0, ymin, ymax):
    b = vy_0 + 1 / 2
    min_t = b + sqrt(b ** 2 - 2 * ymax)
    max_t = b + sqrt(b ** 2 - 2 * ymin)
    return list(range(ceil(min_t), floor(max_t) + 1))


def x_at(t, vx_0):
    t = min(t, vx_0)
    return (vx_0 + 1 / 2) * t - t ** 2 / 2


def hits(vx_0, vy_0, target_area):
    xmin, xmax, ymin, ymax = target_area
    for t in t_range(vy_0, ymin, ymax):
        if xmin <= x_at(t, vx_0) <= xmax:
            return True
    return False


# vy = 0 when t = vy_0. Evaluate y(vy_0)
def apex(v_0):
    return int((v_0 ** 2 + v_0) / 2)


def min_vx(xmin):
    return int(1 / 2 + sqrt(1 / 4 + 2 * xmin))


# Slighly optimized brute force
def best_shot(target_area):
    xmin, xmax, ymin, ymax = target_area
    for vy_0 in reversed(range(ymin, 1000)):
        for vx_0 in range(min_vx(xmin), xmax + 1):
            if hits(vx_0, vy_0, target_area):
                return apex(vy_0)
    return None


if __name__ == "__main__":
    target_area = (128, 160, -142, -88)

    print(best_shot(target_area))
