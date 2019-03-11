def fib(n):
    # basic cases
    if n<0:
        print("n have to be positive!")
        return -1
    if n==0: return []
    if n==1: return [1]
    if n==2: return [1,1]

    # higher cases
    l = [1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l

num = int(input("Give a positive number: "))

print(fib(num))

