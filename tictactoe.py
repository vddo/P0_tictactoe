"""
Tic Tac Toe Player
"""

import math
import copy
# import sys # May be needed


# Define classes
class Move():
    def __init__(self, score, action):
        self.score = score  # Current board
        # self.depth = depth  # Last board before action
        self.action = action  # Action that resulted in board


# define possible moves
X = "X"
O = "O"
EMPTY = None

# Define depth-limit
depth_limit = math.inf

# Define frontier like move set
# move_set = []

# Visualization of board


def print_board(board):
    for i in range(3):
        print(board[i])
    return


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# Create inital board as class State
# start = State(boardState=initial_state(), parent=None, action=None)
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
    countX = player_count(board, X)
    countO = player_count(board, O)
    # countTurn = countX + countO
    if countX == countO:
        return X
    elif countO - countX == 1:
        return X
    elif countX - countO == 1:
        return O
    else:
        raise Exception("Some thing wrong with player function")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    B = copy.deepcopy(board)
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
    B = copy.deepcopy(board)
    actionList = actions(board)
    if action in actionList:
        i, j = action
    else:
        raise Exception("Square taken!")
    # currentPlayerTurn, playedTurns = player(board)
    B[i][j] = player(board)
    # played_actions.add(action)
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
    elif board[1][1] is not None and \
            board[1][1] == board[1][0] == board[1][2]:
        return board[1][1]
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
        return board[1][2]
    elif board[1][1] is not None and \
            board[1][1] == board[0][1] == board[2][1]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:    # Necessary that winner()
        return True                  # is beeing called

    k = 0
    for i in range(3):
        k = k + board[i].count(None)
    if k == 0:
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        score = winner(board)    # Necessary that winner()
        if score == X:                      # is beeing called?
            return 1
        elif score == O:
            return -1
        elif score is None:
            return 0
        else:
            raise Exception("utility() is not working correctly!")


def evaluation(board):
    """
    Calculate estimate utlity of non terminal board as score.
    """
    score = 0
    return score


def max_value(board, depth):
    print_board(board)
    print("I'm in max_value.")
    print(terminal(board))

    depth += 1
    print(depth)

    if terminal(board):
        return utility(board)

    v = -math.inf
    action_list = actions(board)
    # action_evaluated = dict()
    move_set2 = []

    if depth < depth_limit:
        if depth == 1:
            for action in action_list:
                minimum = min_value(result(board, action), depth)
                move_set2.append(Move(score=minimum, action=action))
                v = max(v, minimum)
        else:
            for action in action_list:
                minimum = min_value(result(board, action), depth)
                v = max(v, minimum)
    else:
        v = evaluation(board)
    # if depth == 2:
    #     move_set.append(v)
    # print(len(move_set))
    # if len(move_set2) > 0:
    #     print("here!")
    #     for move in move_set2:
    #         print(move.score, move.action)
    if depth == 1:
        return((v, move_set2))
    else:
        return v


def min_value(board, depth):
    print_board(board)
    print("I'm in min_value.")
    print(terminal(board))

    depth += 1
    print(depth)

    if terminal(board):
        return utility(board)

    v = math.inf
    action_list = actions(board)
    move_set2 = []

    if depth < depth_limit:

        if depth == 1:
            for action in action_list:
                maximum = max_value(result(board, action), depth)
                move_set2.append(Move(score=maximum, action=action))
                v = min(v, maximum)
        else:
            for action in action_list:
                maximum = max_value(result(board, action), depth)
                v = min(v, maximum)

    else:
        v = evaluation(board)

    # if depth == 2:
    #     move_set.append(v)
    # print(len(move_set))
    # if len(move_set2) > 0:
    #     print("here!")
    #     for move in move_set2:
    #         print(move.score, move.action)
    if depth == 1:
        return((v, move_set2))
    else:
        return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    depth = 0
    # reset move_set
    # move_set.clear()

    if turn == X:
        v, move_set2 = max_value(board, depth)
    elif turn == O:
        v, move_set2 = min_value(board, depth)
    else:
        raise Exception("Error: nobodys turn")

    print("\n\n\n\n\n\n\n")
    print(v)
    for move in move_set2:
        print(move.action)

    # for i in action_evaluated:
    #     if i[0] == v:
    #         next_move_ai = i[1]

    for move in move_set2:
        if move.score == v:
            return move.action
    else:
        raise Exception("No move!")
