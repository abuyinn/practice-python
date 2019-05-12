#!/usr/bin/env python3

import random
import string

#######################
# Cows And Bulls game #
#######################

#########
# CONSTS
str_len = 4

############
# FUNCTIONS

def guessing_result(_real_num, _guess):
    cows  = 0
    bulls = 0

    # remaining: not cows hit
    remaining_real_num = []
    remaining_guess    = []


    # check length
    if len(_guess) < str_len:
        return "Guess too short."

    # count the cows:
    for i in range(str_len):
        if _real_num[i] == _guess[i]: cows+=1
        else:
            remaining_real_num.append(_real_num[i])
            remaining_guess.append(_guess[i])
    
    # count the bulls:
    for c in remaining_real_num:
        if c in remaining_guess:
            bulls+=1
            remaining_guess.remove(c)

    # return nice result:
    return (('C'*cows) +
            ('B'*bulls) +
            ('.'*(str_len-cows-bulls)))

#######
# MAIN
if __name__ == "__main__":
    hit     = False
    real_num= ''.join([random.choice(string.digits) for _ in range(str_len)])
    zeros   = str_len*'0'
    nines   = str_len*'9'
    c_s     = str_len*'C'
    guesses = 0

    print("Cows and Bulls Game.")

    while not hit:
        guess   = input("\nGuess the number ("+zeros+"-"+nines+"): ")
        guesses+=1
        res     = guessing_result(real_num, guess)
        print(res)
        if res == c_s:
            print("\nCongratulations! You win!\nIt takes you",guesses,"guesses.")
            hit = True

