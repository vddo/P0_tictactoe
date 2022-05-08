"""
Starting with imports
"""
import tictactoe as ttt
import sampleBoards as sb


"""
Testing the modules in ttt
"""
ttt.terminal(sb.board_diagWinnerX)
ttt.utility(sb.board_diagWinnerX)

ttt.terminal(sb.board_winner_horizontal_X)
ttt.utility(sb.board_winner_horizontal_X)

ttt.terminal(sb.board_winner_none)
ttt.utility(sb.board_winner_none)

ttt.terminal(sb.board_draw)
ttt.utility(sb.board_draw)
