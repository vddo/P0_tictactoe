from tictactoe import initial_state as inst
from tictactoe import player
import tictactoe as ttt

def print_board(board):
    for i in range(3):
        print(board[i])


state_0 = inst()

state_0
ex_0 = [[0, 0], [0, 0]]

state_x_wins = [["X", "X", "O"], ["O", "X", "X"], ["X", "X", "X"]]
print(state_x_wins)


print_board(state_x_wins)

k = 0

for i in ex_0:
    k += i.count(0)
    print(k)


def kcount(inp, val):
    k = 0
    for i in inp:
        k += i.count(val)
    return k


kcount(state_x_wins, "X")

kcount(state_0, "X") == kcount(state_0, "O")
kcount(state_x_wins, "X") == kcount(state_x_wins, "O")


kk = kcount(state_x_wins, "X")

##########################
if kcount(state_0, "X") == kcount(state_0, "O"):
    print("payer X turn")
elif kcount(state_0, "X") - kcount(state_0, "O") == 1:
    print("player O turn")
else:
    print("some thing wrong with player function")
##########################


def playerx(state):
    if kcount(state, "X") == kcount(state, "O"):
        print("payer X turn")
    elif kcount(state, "X") - kcount(state, "O") == 1:
        print("player O turn")
    else:
        raise Exception("some thing wrong with player function")
    return


playerx(state_x_wins)

state_many_Os = [["O", "O", "O"], ["O", "X", "X"], ["O", "X", "O"]]

playerx(state_many_Os)

state_diag_winner = [["O", "O", "X"], ["O", "X", "X"], ["X", "X", "O"]]


def winner_diag(board):
    B = board
    # print_board(board)
    k = False
    P = ['X', 'O']
    if B[1][1] == 'Empty':
        return None
    for player in P:
        if B[1][1] == player:
            #print('chu')
            if B[0][0] == player:
                #print('chu-chu')
                if B[2][2] == player:
                    return player
            elif B[0][2] == player:
                #print('chu-chu')
                if B[2][0] == player:
                    return player
        else:
            return None


winner_diag(state_diag_winner)


class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("emtpy frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


"""
Working von def actions
with index() -> return index, but only for first hit
and count() -> counts how often target appears
"""
state_0 = inst()
state_diag_winner = [["O", "O", "X"], ["O", "X", "X"], ["X", "X", "O"]]
print_board(state_diag_winner)
state_0[0][0] = "X"
print_board(state_0)

state_diag_winner[0].index('X')
state_0[0].index('X')

# Return action of first row
state_0[0].count(None)
state_0[0].index(None)
print(state_0[0])


state_0 = inst()
state_0[0][0] = "X"
state_0[0][1] = "X"
print_board(state_0)
state_0[0].count(None)
state_0[0].index(None)

list_of_actions = []
controll_i = []
controll_index = []
i = 0
k = state_0[0].count(None)
while i < k:
    list_of_actions.append(state_0[0].index(None))
    controll_i.append(i)
    controll_index.append(state_0[0].index(None))
    state_0[0][state_0[0].index(None)] = "done"
    i += 1

print(list_of_actions)
print(k)
print(controll_i)
print(controll_index)


print_board(state_0)


# Test with all 3 rows

B_05 = [[None, None, None], [None, "X", None], [None, None, None]]
print_board(B_05)

B00 = copy.deepcopy(B_05)

B00[0][0] = "X"

print(B_05)
print(B00)

L_actions = []


for i in range(3):
    j = 0
    k = B_05[i].count(None)
    print(i, k)
    while j < k:
        L_actions.append([i, B_05[i].index(None)])
        B_05[i][B_05[i].index(None)] = "done"
        j += 1


print(L_actions)

# function

import copy

def actions(board):
    B = copy.deepcopy(board)
    L = []  # List of actions
    for i in range(3):
        j = 0
        k = B[i].count(None)
        while j < k:
            L.append([i, B[i].index(None)])
            B[i][B[i].index(None)] = "done"
            j += 1
    return L


L_ = actions(B_05)
print_board(B_05)
print(L_)


"""
Paragraph 2
"""

ttt.Move(action=1, score=0)

b = []
b.append(ttt.Move(action=34, score=98))

b[0].action
