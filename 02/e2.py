#####################
print("First part\n")

number = int(input("Give a number: "))

if number%2==0:
    if number%4==0:
        print("This number is a multiplication of 4.")
    else:
        print("This number is even.")
else:
    print("This number is odd.")


##########################
print("\n\nSecond part\n")

# I dont understand naming in this task.
num   = int(input("Give a number 'num':   "))
check = int(input("Give a number 'check': "))

if num!=0:
    if check%num == 0:
        print("Check divides evenly by num.")
    else:
        print("Check doesn't divides evenly by num.")
else:
    print("Use other num next time.")

