import time
from cachetools import LRUCache

from Board import Board
from Solver import solve
from termcolor import colored


def main():
    difficulty = input("Enter difficulty easy (e), medium (m), or hard (h): ")
    match difficulty:
        case "e":
            depth = 4
            random_move_chance = .3
        case "m":
            depth = 7
            random_move_chance = .1
        case "h":
            depth = 11
            random_move_chance = 0
        case _:
            print(colored("Invalid difficulty. Must be 'e', 'm', or 'h'", "red"))
            return
    c4 = Board()
    print(c4)
    tt = LRUCache(maxsize=1000000)
    while True:
        move = input(f"Player {c4.current_player()}. Input move: ")
        move = str(int(move.strip()) - 1)
        was_played, result = c4.play(move)
        print(c4)
        if not was_played:
            print(colored("Invalid move", "red"))
            continue
        if result:
            print(colored(f"Player {result} won!", "green"))
            return
        start_time = time.time()
        score, col = solve(c4, tt, depth=depth, random_move_chance=random_move_chance)
        print("score: ", score)
        print("optimal move: ", col)
        print(f"Time taken: {time.time() - start_time}")
        was_played, result = c4.play(str(col))
        print(c4)
        if not was_played:
            print(colored("AI made invalid move", "red"))
            return
        if result:
            print(colored(f"Player {result} won!", "green"))
            return
        if c4.is_full():
            print("Draw")
            break

if __name__ == "__main__":
    main()