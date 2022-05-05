"""
Tic Tac Toe Player
"""

import math
import copy
# import sys # May be needed

# Define classes


class State():
    def __init__(self, boardState, parent, action):
        self.boardState = boardState  # Current board
        self.parent = parent  # Last board before action
        self.action = action  # Action that resulted in board


# define possible moves
X = "X"
O = "O"
EMPTY = None

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


# Create inital board as class State
start = State(boardState=initial_state(), parent=None, action=None)
played_actions = set()


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
    countX = player_count(board.board, X)
    countO = player_count(board, O)
    countTurn = countX + countO
    if countX == countO:
        return X
    elif countX - countO == 1:
        return O
    else:
        raise Exception("Some thing wrong with player function")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    B = copy.deepcopy(board.boardState)
    # B = board.boardState
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
    B = copy.deepcopy(board.boardState)
    actionList = actions(board.boardList)
    if action in actionList:
        i, j = action
    else:
        raise Exception("Square taken!")
    # currentPlayerTurn, playedTurns = player(board)
    B[i][j] = player(board.boardState)
    played_actions.add(action)
    return B


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking for diagonal win
    if board[1][1] is not None:
        if board[0][0] == board[1][1] == board[2][2] \
                or board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    # else:
    #     return None

    # Checking for horizontal win
    if board[0][1] is not None and \
            board[0][1] == board[0][0] == board[0][2]:
        return board[0][1]
    elif board[2][1] is not None and \
            board[2][1] == board[2][0] == board[2][2]:
        return board[2][1]
    # else:
    #     return None

    # Checking vor vertical win
    # if horizontal check would have been a function:
    # def winner_vertically2(board):
    #    return winner_horizontally(list(map(list, zip(*board))))
    # function winner_vertically2 tranposes board and calls horizontal check
    if board[1][0] is not None and \
            board[1][0] == board[0][0] == board[2][0]:
        return board[1][0]
    elif board[1][2] is not None and \
            board[1][2] == board[0][2] == board[2][2]:
        return board[2][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board.boardState) is not None:    # Necessary that winner()
        return True                             # is beeing called
    elif board.boardState.count(None) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board.boardState):
        score = winner(board.boardState)    # Necessary that winner()
        if score == X:                      # is beeing called?
            return 1
        elif score == O:
            return -1
        elif score is None:
            return 0
        else:
            raise Exception("utility() is not working correctly!")


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
    raise NotImplementedError
    raise NotImplementedError
    raise NotImplementedError
    raise NotImplementedError
