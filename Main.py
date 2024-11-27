from Board import Board
from Solver import solve


def main():
    c4 = Board()
    print(c4)
    moves = input("Input move: ")
    c4.play(moves)
    print(c4)
    score = solve(c4)
    print(score)


if __name__ == "__main__":
    main()