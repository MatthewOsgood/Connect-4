import time
import numpy as np
from Board import Board
from Solver import solve
from termcolor import colored


def main():
    difficulty = input("Enter difficulty easy (e), medium (m), or hard (h): ")
    if difficulty is "e":
        depth = 4
    elif difficulty is "m":
        depth = 7
    elif difficulty is "h":
        depth = 11
    else:
        print(colored("Invalid difficulty. Must be 'e', 'm', or 'h'", "red"))
        return
    c4 = Board()
    print(c4)
    while True:
        moves = input(f"Player {c4.current_player()}. Input move: ")
        was_played, result = c4.play(moves)
        print(c4)
        if not was_played:
            continue
        if result:
            print(colored(f"Player {result} won!", "green"))
            return
        start_time = time.time()
        score, col = solve(c4, depth=depth)
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