from Board import Board
from Solver import solve


def main():
    depth = int(input("Enter max depth: "))
    c4 = Board()
    print(c4)
    while True:
        moves = input(f"Player {c4.current_player()}. Input move: ")
        c4.play(moves)
        print(c4)
        score, col = solve(c4, depth=depth)
        print("score: ", score)
        print("optimal move: ", col)

if __name__ == "__main__":
    main()