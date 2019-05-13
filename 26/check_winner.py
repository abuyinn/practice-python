#!/usr/bin/env python3

# Note: the check functions return:
#   False:  if noone is win
#   1:      if player 1 win
#   2:      if player 2 win

def transpose(_board):
    return [list(e) for e in zip(* _board)]

def check_horizontal(_board):
    for row in _board:
        x=row[0]
        if x:
            if x==row[1] and x==row[2]:
                return x
    return False

def check_vertical(_board):
    return check_horizontal(transpose(_board))

def check_diagonal(_board):
    mid=_board[1][1]
    if mid:
        if mid==_board[0][0] and mid==_board[2][2]: return mid
        if mid==_board[0][2] and mid==_board[2][0]: return mid
    return False

def check_winner(_board):
    #check horizontal:
    h = check_horizontal(_board)
    if h: return h

    # check vertical:
    v = check_vertical(_board)
    if v: return v

    # check diagonal:
    return check_diagonal(_board)

