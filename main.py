from chess import Board, King, Queen, Bishop, Knight, Rook, Pawn
from Interfaces import ConsoleInterface, TextInterface
import curses
ui = TextInterface()
game = Board(debug=False, inputf=ui.get_player_input, printf=ui.set_msg)

if game.debug:
    game.start()
    ui.set_msg("New game started.")
    while game.winner is None:
        ui.set_msg('== DISPLAY ==')
        ui.set_board(game.display())
        ui.set_msg('== PROMPT ==')
        while True:
          start, end = game.prompt()
          if game.valid_move(start, end):
            break
          else:
            ui.set_msg(f"Invalid Move: {start} -> {end}")
        ui.set_msg('== UPDATE ==')
        game.update(start, end)
        ui.set_msg('== NEXT TURN ==')
        game.next_turn()
else:
    game.start()
    ui.set_msg("New game started.")
    while game.winner is None:
        ui.set_board(game.display())
        while True:
          start, end = game.prompt()
          if game.valid_move(start, end):
            break
          else:
            ui.set_msg(f"Invalid Move: {start} -> {end}")
        game.update(start, end)
        game.next_turn()
game.display()
ui.set_msg(f'Game over. {game.winner} player wins!')
