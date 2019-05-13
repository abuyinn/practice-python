#!/usr/bin/env python3
import math

TOOSMALL = '1'
TOOBIG   = '2'
EQUAL    = '3'
ERROR    = 'error'

def make_guess(_fst, _lst):
    if _fst>_lst: return ERROR
    return math.ceil(_fst + (_lst-_fst)/2)

if __name__=="__main__":
    print("Choose your number (0-100). I'll be guessing.")
    input("Press enter if you're ready!")

    guessed = '0'   # when computer hit the number it will be '3'
    guesses =   0   # how much time program make a guess
    fst     =   0   # first possible number
    guess   =  50   # program's next test
    lst     = 100   # last possible number

    while guessed!=EQUAL and guess!=ERROR:
        guesses+=1
        guessed=input("\nMy guess ("+str(fst)+","+str(lst)+"): "+str(guess)+"\n"
                      "["+TOOSMALL+"] Too small\n"
                      "["+TOOBIG+  "] Too big\n"
                      "["+EQUAL+   "] That's it!\n")
        if guessed==TOOSMALL: fst = guess+1
        if guessed==TOOBIG:   lst = guess-1
        guess = make_guess(fst, lst)

    print("\nIt takes me",guesses,"guesses.")
    if guess==ERROR: print("...to know you're a cheater!")

