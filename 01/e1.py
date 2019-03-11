import datetime

# get data
name =     input("enter your name: ")
age  = int(input("enter your age:  "))
num  = int(input("enter a number:  "))

# count year
currentyear = datetime.datetime.now().year
dateofbirth = currentyear-age
date100yo   = str(dateofbirth+100)

# print messages
print(("\nYou will have 100 yo in "+date100yo+", "+name+".")*num)

