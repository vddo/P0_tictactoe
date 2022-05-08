import tictactoe as ttt
import sampleBoards as sb

print(ttt.print_board(sb.board_winner_none))

print(ttt.minimax(sb.board_winner_none))

ttt.player(sb.board_winner_none)
