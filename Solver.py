from Board import Board
from cachetools import LRUCache
# from random import random
from numpy import random


def negamax(b: Board, alpha, beta, transposition_table: LRUCache, depth=9999) -> int:
    if depth is not None and depth == 0:
        return b.heuristic_value()
    if b.is_full():
        return 0
    for col in range(Board.WIDTH):
        if b.can_play(col) and b.is_winning_move(col):
            return 100 - b.moves
    
    max_score = (Board.WIDTH * Board.HEIGHT - 1 - b.moves) // 2
    val = transposition_table.get(b.board.tobytes())
    if val is not None:
        max_score = val + Board.MIN_SCORE
        
    if beta > max_score:
        beta = max_score
        if alpha >= beta: 
            return beta
    for col in Board.SEARCH_ORDER: # search middle columns first b/c they tend to be better
        if b.can_play(col):
            b2: Board = b.copy()
            b2.drop_piece(col)
            score = -negamax(b2, -beta, -alpha, transposition_table, depth=depth-1)
            if score >= beta:
                return score
            alpha = max(score, alpha)
    transposition_table[b.board.tobytes()] = alpha - Board.MIN_SCORE + 1
    return alpha

def solve(board: Board, depth=9999, random_move_chance=0):
    """
    :return the column with the best possible move
    """
    tt = LRUCache(maxsize=1000000)
    alpha = -(board.WIDTH * board.HEIGHT // 2)
    beta = -alpha
    for col in range(Board.WIDTH):
        if board.can_play(col) and board.is_winning_move(col):
            return 100, col
    boards = [(board.copy(), col) for col in Board.SEARCH_ORDER if board.can_play(col)]
    if  random.random() <= random_move_chance:
        return 0, random.choice(board)[1]
    
    for b, col in boards:
        b.drop_piece(col)
    scores = [(-negamax(b, alpha, beta, tt, depth=depth), col) for b, col in boards]
    return max(scores, key=lambda x: x[0])