from Board import Board

def negamax(b: Board, alpha, beta, max_depth=None) -> int:
    assert(alpha < beta)
    if b.is_full():
        return 0
    for col in range(Board.WIDTH):
        if b.can_play(col) and b.is_winning_move(col):
            return (Board.WIDTH * Board.HEIGHT + 1 - b.moves) // 2
    
    max_score = (Board.WIDTH * Board.HEIGHT - 1 - b.moves) // 2
    if beta > max_score:
        beta = max_score
        if alpha >= beta: 
            return beta
    for col in Board.SEARCH_ORDER: # search middle columns first b/c they tend to be better
        if b.can_play(col):
            b2: Board = b.copy()
            b2.drop_piece(col)
            score = -negamax(b2, -beta, -alpha)
            if score >= beta:
                return score
            alpha = max(score, alpha)
    return alpha

def solve(board: Board, max_depth=None):
    """
    :return the column with the best possible move
    """
    alpha = -(board.WIDTH * board.HEIGHT // 2)
    beta = -alpha
    boards = [(board.copy(), col) for col in Board.SEARCH_ORDER if board.can_play(col)]
    for b, col in boards:
        b.drop_piece(col)
    scores = [(-negamax(b, alpha, beta, max_depth=max_depth), col) for b, col in boards]
    return max(scores, key=lambda x: x[0])