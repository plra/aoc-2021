def advance(space, roll):
    return (space + roll) % 10 or 10


def next_roll(roll):
    return roll + 1 if roll < 100 else 1


def play(p1_start, p2_start):
    spaces = [p1_start, p2_start]
    scores = [0, 0]
    n_rolls = 0
    roll = 0
    while True:
        for player in [0, 1]:
            for _ in range(3):
                roll = next_roll(roll)
                n_rolls += 1
                spaces[player] = advance(spaces[player], roll)
            scores[player] += spaces[player]
            if scores[player] >= 1000:
                return scores[1 - player] * n_rolls


if __name__ == "__main__":
    print(play(8, 4))

