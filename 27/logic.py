#!/usr/bin/env python3

X = 'X'  # 1st player
O = 'O'  # 2nd player

def int2sign(_i):
    if _i==0: return " "
    if _i==1: return X
    if _i==2: return O
    else:     return "?"

def isFree(row,col,_board,_size):
    if row<0 or col<0 or row>=_size or col>=_size:
        return False
    return _board[row][col]==0

def move2tuple(move):
    if ',' in move: return tuple([  int(s) for s in move.split(",")  ][:2])
    else:           return (-1,-1)

def get_move(_player, _board, _move_number, _size):
    while True:
        move = input("\n\n#"+str(_move_number)+"  Player "+int2sign(_player)+"\n"
                         "Write 'row,col': ")
        (row,col) = move2tuple(move)
        
        if isFree(row,col,_board,_size):
            return (row,col)
        else:
            print("Cell invalid or occupied. Choose again.")



