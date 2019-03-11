import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = [i for i in a if i in b]
unique_common = list(set(common))

print(unique_common)


#Extra 1&2
a = [random.randrange(10) for i in range(random.randrange(5,15))]
b = [random.randrange(10) for i in range(random.randrange(5,15))]

print("\na =",a,"\nb =",b,"\nc =",
        list(set(  [i for i in a if i in b]  )) )

