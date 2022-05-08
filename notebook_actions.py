"""
notebook to work on function actions
Returns set of all possible actions (i, j)
available on the board.
"""

# Import functions
import tictactoe as ttt
import copy


# def print_board(board):
#     for i in range(3):
#         print(board[i])
# Already included in main function ttt


def actions(board):
    B = copy.deepcopy(board)
    L = []  # List of actions
    for i in range(3):
        j = 0
        k = B[i].count(None)
        while j < k:
            L.append((i, B[i].index(None)))
            B[i][B[i].index(None)] = "done"
            j += 1
    return L


B01 = [[None, None, None], [None, "X", None], [None, None, None]]
B05 = [[None, None, None], [None, "X", None], [None, None, None]]
ttt.print_board(B_05)

A = actions(B05)
print(A)

B04 = [[None, "X", None], [None, "X", "O"], [None, "O", None]]
ttt.print_board(B04)

actions(B04)

"""
Trying actions() from tictactoe.py
"""


# ttt.initial_state()
ttt.print_board(B04)

print(ttt.EMPTY)

ttt.actions(B04)
ttt.actions(ttt.initial_state())

ttt.player(B04)

# New section
initialState = ttt.initial_state()

ttt.actions(initialState)
