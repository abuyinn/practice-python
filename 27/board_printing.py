#!/usr/bin/env python3
# writing board is different than in 24

from logic import int2sign

def write_horizontal(_size):
    print("  " + " ---"*_size)

def write_vertical(_size, _i, _row):
    print(_i,"| ",end="")
    print(" | ".join(map(int2sign,_row)),end=" |\n")

def write_horizontal_numbers(_size):
    print("   ".join( [' ']+[str(i) for i in range(_size)] ))

def write_board(_size, _board):
    write_horizontal_numbers(_size)
    for i in range(_size):
        write_horizontal(_size)
        write_vertical(_size,i,_board[i])
    write_horizontal(_size)

