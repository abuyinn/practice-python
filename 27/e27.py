#!/usr/bin/env python3

import importlib

import board_printing as bp
import logic as l
exec(open("../26/check_winner.py").read())

SIZE = 3

if __name__=="__main__":
    
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    current_player = 1
    winner = 0

    bp.write_board(SIZE, board)
    
    for move_number in range(1,SIZE*SIZE+1):
        (row,col) = l.get_move(current_player,board,move_number,SIZE)
        board[row][col]=current_player
        bp.write_board(SIZE,board)

        winner = check_winner(board)
        if winner:
            print("\nPlayer",l.int2sign(current_player),"win.")
            break

        current_player = 3-current_player   # other player move

    if not winner:
        print("\nDraw.")

