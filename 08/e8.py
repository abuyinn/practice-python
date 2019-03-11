def get_move(player):
    while True:
        move = input("[r]ock  [p]aper  [s]cisors\nPlayer "+player+": ")
        if move[0]=='r':
            return 'r'
        if move[0]=='p':
            return 'p'
        if move[0]=='s':
            return 's'
        print("Bad move... Try again...")

def get_result(a,b):
    if a==b:       return "Draw"
    if a=='r':
        if b=='p': return "B wins!"
        if b=='s': return "A wins!"
    if a=='p':
        if b=='r': return "A wins!"
        if b=='s': return "B wins!"
    if a=='s':
        if b=='r': return "B wins!"
        if b=='p': return "A wins!"
    

new_game = True

while new_game:
    print("\n\n\n!!! N E W   G A M E !!!")
    a=get_move("A")
    b=get_move("B")
    print(get_result(a,b))

    new_game = input("\nNew game? [y/n]: ")[0] == 'y'

