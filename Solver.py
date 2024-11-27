from Board import Board



def negamax(board: Board, alpha, beta, max_depth=None):
    if board.is_full():
        return 0
    for col in range(Board.width):
        if board.can_play(col) and board.is_winning_move(col):
            return (Board.width * Board.height + 1 - board.moves) // 2
    
    max = (Board.width * Board.height + 1 - board.moves) // 2
    beta = min(beta, max)
    if alpha >= beta: 
        return beta
    for col in [3, 2, 4, 1, 5, 0, 6]: # search middle columns first b/c they tend to be better
        if board.can_play(col):
            b2: Board = board.copy()
            b2.drop_piece(col)
            score = negamax(b2, -beta, -alpha)
            if score >= beta:
                return score
            alpha = max(score, alpha)
    return alpha

def solve(board: Board):
    beta = board.width * board.height // 2
    alpha = -beta
    return negamax(board, alpha, beta)