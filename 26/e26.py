#!/usr/bin/env python3

import check_winner as cw

if __name__=="__main__":
    winner_is_1 =  [[1, 2, 0],
                    [2, 1, 0],
                    [2, 1, 1]]
    winner_is_1_ = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]
    winner_is_2 =  [[2, 2, 0],
                    [2, 1, 0],
                    [2, 1, 1]]
    winner_is_2_ = [[0, 1, 0],
                    [1, 2, 0],
                    [2, 2, 2]]
    no_winner =    [[1, 2, 0],
                    [2, 1, 0],
                    [2, 1, 2]]
    no_winner_ =   [[1, 2, 0],
                    [2, 1, 0],
                    [2, 1, 0]]

    print("winner_is_1:\t", cw.check_winner(winner_is_1))
    print("winner_is_1_:\t",cw.check_winner(winner_is_1_))
    print("winner_is_2:\t", cw.check_winner(winner_is_2))
    print("winner_is_2_:\t",cw.check_winner(winner_is_2_))
    print("no_winner:\t",   cw.check_winner(no_winner))
    print("no_winner_:\t",  cw.check_winner(no_winner_))

