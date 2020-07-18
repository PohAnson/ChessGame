from chess import *
import sys

def mini_board():
    game = Board(debug=True)
    game.start()
    game.position = {}
    game.add((0,7), King('white'))
    game.add((0,5), King('black'))
    game.add((3,5), Pawn('white'))
    a = Queen
    game.add((6,2), a('black'))
    game.turn = 'black'
    while game.winner is None:
        game.display()
        start, end = game.prompt()
        # print('====Display====')
        # game.display()
        game.update(start, end)
        game.next_turn()
    print(f'Game over. {game.winner} player wins!')

#input to use for testing of mini-board
# mini_board()
#62 35
#07 17
# 35 37

# checking for full board checkmate
""" 
41 42
06 05
50 23
05 04
30 52
04 03
23 56

white pawn 41 -> 42
black pawn 06 -> 05
white bishop 50 -> 23
black pawn 05 -> 04
white queen 30 -> 52
black pawn 04 -> 03
white bishop 23 -> 56
"""