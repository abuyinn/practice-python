import random

next_guess = True
num        = random.randrange(1,10)
guesses    = 0

while next_guess:
    guess = input("Guess the number (or type 'e' to exit): ")

    if guess == '':
        # let try again
        None
    elif guess[0]=='e':
        print("Closing...")
        next_guess=False
    else:
        guess=int(guess)
        guesses+=1
        if guess == num:
            print("That's it! It takes you",guesses,"guesses!\n\n\n"
                    "Generating new number...")
            num     = random.randrange(1,10)
            guesses = 0
        elif guess>num:
            print("No, too high.")
        elif guess<num:
            print("No, too low.")

