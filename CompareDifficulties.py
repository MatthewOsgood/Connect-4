from cachetools import LRUCache

from Board import Board
from Solver import solve


def compare_difficulties(depth1, random_move_chance1, depth2, random_move_chance2):
    tt1 = LRUCache(maxsize=1000000)
    tt2 = LRUCache(maxsize=1000000)
    p1_wins = 0
    p1_losses = 0
    for _ in range(20):
        c4 = Board()
        while True:
            score, col = solve(c4, tt1, depth=depth1, random_move_chance=random_move_chance1)
            was_played, result = c4.play(str(col))
            if not was_played:
                Exception("AI made invalid move")
            if result == Board.MAX:
                p1_wins += 1
                break
            if result == Board.MIN:
                p1_losses += 1
                break
            score, col = solve(c4, tt2, depth=depth2, random_move_chance=random_move_chance2)
            was_played, result = c4.play(str(col))
            if not was_played:
                Exception("AI made invalid move")
            if result == Board.MAX:
                p1_wins += 1
                break
            if result == Board.MIN:
                p1_losses += 1
                break
            if c4.is_full():
                break
    return p1_wins, p1_losses


def main():
    with open("results.txt", "w") as f:
        p1_wins, p1_losses = compare_difficulties(7, .1, 4, .3)
        print(f"M vs E wins: {p1_wins}, losses: {p1_losses}")
        f.write(f"M vs E wins: {p1_wins}, losses: {p1_losses}\n")

        p1_wins, p1_losses = compare_difficulties(11, 0, 4, .3)
        print(f"H vs E wins: {p1_wins}, losses: {p1_losses}")
        f.write(f"H vs E wins: {p1_wins}, losses: {p1_losses}\n")

        p1_wins, p1_losses = compare_difficulties(11, 0, 7, .1)
        print(f"H vs M wins: {p1_wins}, losses: {p1_losses}")
        f.write(f"H vs M wins: {p1_wins}, losses: {p1_losses}\n")



if __name__ == "__main__":
    main()