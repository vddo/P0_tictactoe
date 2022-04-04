"""
Tic Tac Toe Player
"""

import math
import copy

# define possible moves
X = "X"
O = "O"
EMPTY = None

## Notebook
# class Board():
#     """
#     class Board like Node in maze.py
#     """
#
#     def __init__(self, board, parent, action, players_turn):
#         self.board = board
#         self.parent = parent
#         self.action = action
#         self.players_turn = players_turn

def print_board(board):
    for i in range(3):
        print(board[i])

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player_count(board, valueXO):
    k = 0
    for i in board:
        k += i.count(valueXO)
    return k


def player(board):
    """
    Returns player who has the next turn on a board.
    Count number auf "X" and "O". X-Player will start therefor if number
    is equal X-Players turn. If more "X"s it's O-Players turn.
    """
    if player_count(board, X) == player_count(board, O):
        return X
    elif player_count(board, X) - player_count(board, O) == 1:
        return O
    else:
        raise Exception("some thing wrong with player function")
    return


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    B = copy.deepcopy(board)
    L = []   # List of actions
    for i in range(3):
        j = 0
        k = B[i].count(None)
        while j < k:
            L.append([i, B[i].index(None)])
            B[i][B[i].index(None)] = "done"
            j += 1
    return L


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
    raise NotImplementedError
    raise NotImplementedError
    raise NotImplementedError
    raise NotImplementedError
