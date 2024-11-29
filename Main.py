import numpy as np
from Board import Board
from Solver import solve
from termcolor import colored


def main():
    depth = int(input("Enter difficulty from 1-10: "))
    if not 1 <= depth <= 10:
        print("Invalid difficulty")
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
        score, col = solve(c4, depth=depth)
        print("score: ", score)
        print("optimal move: ", col)
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