"""
Imports
"""
import sampleBoards as sb
from tictactoe import winner
import tictactoe as ttt


"""
Functions in work
"""


def winner_diag(board):
    B = board
    P = ['X', 'O']
    if B[1][1] is None:
        return None
    for player in P:
        if B[1][1] == player:
            if B[0][0] == player:
                if B[2][2] == player:
                    return player
            elif B[0][2] == player:
                if B[2][0] == player:
                    return player
        else:
            return None


def winner_diag2(board):
    center = board[1][1]
    if center is None:
        return None
    elif board[0][0] == center == board[2][2] \
            or board[0][2] == center == board[2][0]:
        return center
    else:
        return None


def winner_horizontally(board):
    if board[0][1] is not None and \
            board[0][1] == board[0][0] == board[0][2]:
        return board[0][1]
    elif board[2][1] is not None and \
            board[2][1] == board[2][0] == board[2][2]:
        return board[2][1]
    else:
        return None


def winner_vertically(board):
    if board[1][0] is not None and \
            board[1][0] == board[0][0] == board[2][0]:
        return board[1][0]
    elif board[1][2] is not None and \
            board[1][2] == board[0][2] == board[2][2]:
        return board[2][1]
    else:
        return None


def winner_vertically2(board):
    return winner_horizontally(list(map(list, zip(*board))))


def winner(board):
    if winner_diag(board) is not None:
        return winner_diag(board)
    print("nope")


def neighbors(cell):
    row, col = cell
    candidates = [
        ("right", (row, col + 1)),
        ("down", (row + 1, col))
    ]


"""
Workspace
"""
sB.board_diagWinnerX
ttt.print_board(sB.board_diagWinnerX)

winner_diag(sB.board_diagWinnerX)
winner_diag(sB.board_11empty)
winner_diag(sB.board_11O)

ttt.print_board(sB.board_11O)
ttt.print_board(sB.board_row1WinnerO)
winner_diag(sB.board_row1WinnerO)

winner(sB.board_diagWinnerX)

winner_diag2(sB.board_diagWinnerX)

if sB.board_row1WinnerO[0][1] == sB.board_row1WinnerO[0][0] == sB.board_row1WinnerO[0][2]:
    print("yes!")


winner_horizontally(sB.board_winner_horizontally)

ttt.print_board(sB.board_winner_horizontally)

ttt.print_board(list(map(list, zip(*sB.board_winner_horizontally))))

list(map(list, zip(*sB.board_winner_horizontally)))

winner_vertically2(sB.board_winner_horizontally)
winner_horizontally(list(map(list, zip(*sB.board_winner_horizontally))))


"""
Testing implementation in tictactoe.py winner()
"""
winner(sb.board_diagWinnerX)
winner(sb.board_winner_horizontal_X)
winner(sb.board_winner_vertical_O)
winner(sb.board_winner_none)
