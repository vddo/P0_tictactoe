"""
Various boards
"""
from tictactoe import print_board


board_diagWinnerX = [["O", "O", "X"], ["O", "X", "X"], ["X", "X", "O"]]
board_11empty = [["O", "O", "X"], ["O", None, "X"], ["X", "X", "O"]]
board_11O = [["O", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
board_winner_horizontal_X = [
    ["O", None, "O"], ["O", "O", "X"], ["X", "X", "X"]]

board_winner_vertical_O = [
    ["O", None, "O"], ["O", None, "X"], ["O", "X", "X"]]

board_winner_none = [
    ["O", None, "O"], ["O", "O", "X"], [None, "X", "X"]]

board_draw = [
    ["O", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]


# print_board(board_winner_none)
