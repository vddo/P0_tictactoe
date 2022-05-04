"""
Tic Tac Toe Player
"""

import math
import copy
# import sys # May be needed

# Define classes


class State():
    def __init__(self, board, parent, action):
        self.board = board  # Current board
        self.parent = parent # Last board before action
        self.action = action # Action that resulted in board
        


# define possible moves
X = "X"
O = "O"
EMPTY = None

# board list to save all resulted boards
"""
Local variable boardList;
[dict]
used to store: (keys) = turns played before result(); (values) = resulting
board after result()
"""
boardList = {}

# Visualization of board


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

# Counts X or O for each cell


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
    countX = player_count(board, X)
    countO = player_count(board, O)
    countTurn = countX + countO
    if countX == countO:
        return X
    elif countX - countO == 1:
        return O
    else:
        raise Exception("some thing wrong with player function")


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
            L.append((i, B[i].index(None)))
            B[i][B[i].index(None)] = "done"
            j += 1
    return L


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    B = copy.deepcopy(board)
    actionList = actions(board)
    #print(actionList)
    if action in actionList:
        i, j = action
    else:
        raise Exception("Square taken!")
    currentPlayerTurn, playedTurns = player(board)
    B[i][j] = currentPlayerTurn
    if not playedTurns in boardList:
        boardList[playedTurns+1] = B
        return B
    else:
        raise Exception("Turn played twice!")


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
