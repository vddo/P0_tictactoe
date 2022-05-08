# bit of try out
import tictactoe as ttt
import copy
import sampleBoards as sb


B0 = ttt.initial_state()
print(B0)

ttt.player(B0)

B01 = copy.deepcopy(B0)

B01[1][1] = ttt.X
B01

ttt.player(B0)

ttt.player(B01)

boardList = ttt.boardList


Atest = (1, 2)

AMatrix = [(2, 2), (1, 2)]

Atest == (1, 2)

AMatrix.count((2, 3))

actionsL = ttt.actions(B01)

actionsL.count((1, 1))


dictTest = {}
dictTest[0] = "EMTPY"
dictTest

0 in dictTest

if not 1 in dictTest:
    print("yes")

dict2 = {0: "X", 1: "O"}

0 in dict2
"X" in dict2
1 in dict2


# ok now for real
"""
def result(board, action):
    ###
    Returns the board that results from making move (i, j) on the board.
    ###
    raise NotImplementedError

in: Board is 3x3 list
    actions is 1x2 list

action = [i, j]
Board[i][j] = X/O

out:    Board = [ [old, old, old], [old, NEW, old], [old, old, old] ]
something like this
"""

A = (0, 2)
i, j = A

boardList = {}
if not boardList:
    print("EMPTY")


# def result(board, action):
#     B = copy.deepcopy(board)
#     actionList = ttt.actions(board)
#     #print(actionList)
#     if actionList.count(action) == 1:
#         i, j = action
#     else:
#         raise Exception("Square taken!")
#     currentPlayerTurn, playedTurns = ttt.player(board)
#     B[i][j] = currentPlayerTurn
#     if not boardList:
#         boardList.append([playedTurns, B])
#     elif boardList[-1][0] != playedTurns:
#         boardList.append([playedTurns, B])
#     return B

# TO BE TESTED
def result(board, action):
    B = copy.deepcopy(board)
    actionList = ttt.actions(board)
    #print(actionList)
    if actionList.count(action) == 1:       # action has to be in list
        i, j = action
    else:
        raise Exception("Square taken!")
    currentPlayerTurn, playedTurns = ttt.player(board)
    B[i][j] = currentPlayerTurn
    if not playedTurns in boardList:
        boardList[playedTurns] = B
        return B
    else:
        raise Exception("Turn played twice!")
##


ttt.actions(sb.board_winner_none)

ttt.result(sb.board_winner_none, (0, 1))

#result(B01, (1, 1))
ttt.result(B0, A)

ttt.boardList

boardList[1]

# test function in tictactoe.py
A02 = (0, 0)

result(boardList[1], A02)

boardList

ttt.result(boardList[1], A)
ttt.boardList


ttt.actions(B0)
if (0, 0) in ttt.actions(B0):
    print("yes")
