from cachetools import LRUCache

from Board import Board
from Solver import solve


def compare_difficulties(depth1, random_move_chance1, depth2, random_move_chance2, tt: LRUCache):
    p1_wins = 0
    p1_losses = 0
    for _ in range(10):
        c4 = Board()
        while True:
            score, col = solve(c4, tt, depth=depth1, random_move_chance=random_move_chance1)
            was_played, result = c4.play(str(col))
            if not was_played:
                Exception("AI made invalid move")
            if result == Board.MAX:
                p1_wins += 1
                break
            if result == Board.MIN:
                p1_losses += 1
                break
            score, col = solve(c4, tt, depth=depth2, random_move_chance=random_move_chance2)
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
    tt = LRUCache(maxsize=1000000) # always use same transposition table to speed things up
    p1_wins, p1_losses = compare_difficulties(7, .1, 4, .3, tt)
    print(f"M vs E wins: {p1_wins}, losses: {p1_losses}")
    p1_wins, p1_losses = compare_difficulties(11, 0, 4, .3, tt)
    print(f"H vs E wins: {p1_wins}, p1 losses: {p1_losses}")
    p1_wins, p1_losses = compare_difficulties(11, 0, 7, .1, tt)
    print(f"H vs M wins: {p1_wins}, losses: {p1_losses}")



if __name__ == "__main__":
    main()