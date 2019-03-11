num = int(input("Give a number: "))

divisors = [i for i in range(1,num+1) if num%i == 0]
print(divisors)

