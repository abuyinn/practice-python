#!/usr/bin/env python3

def write_horizontal(_size):
    print(" ---" * _size)

def write_vertical(_size):
    print("|   " * _size  +"|")

def write_board(_size):
    for i in range(_size):
        write_horizontal(_size)
        write_vertical(_size)
    write_horizontal(_size)

if __name__=="__main__":
    size = int(input("Board's size: "))
    write_board(size)

