a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i<5:
        print(i)

########
#Extra 1
e1 = []
for i in a:
    if i<5:
        e1.append(i)
print(e1)

########
#Extra 2
print([i for i in a if i<5])

########
#Extra 3
num = int(input("Give a number: "))
print([i for i in a if i<num])

