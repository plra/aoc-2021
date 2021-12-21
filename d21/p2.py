from p1 import advance

ROLL_UNIVERSES = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def play(p1_space, p2_space, p1_score=0, p2_score=0, turn="p1", max_score=21):
    if turn == "p2" and p1_score >= max_score:
        return 1, 1
    elif turn == "p1" and p2_score >= max_score:
        return 0, 1

    p1_wins = 0
    universes = 0
    for sum_rolls, new_universes in ROLL_UNIVERSES.items():
        if turn == "p1":
            new_space = advance(p1_space, sum_rolls)
            future_p1_wins, future_universes = play(
                new_space, p2_space, p1_score + new_space, p2_score, turn="p2"
            )
        elif turn == "p2":
            new_space = advance(p2_space, sum_rolls)
            future_p1_wins, future_universes = play(
                p1_space, new_space, p1_score, p2_score + new_space, turn="p1"
            )
        p1_wins += new_universes * future_p1_wins
        universes += new_universes * future_universes

    return p1_wins, universes


if __name__ == "__main__":
    print(play(8, 4))
