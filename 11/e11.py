num = int(input("Give a number: "))

def divisors(num):
    return [i for i in range(1,num+1) if num%i == 0]

if len(divisors(num))==2:
    print("Prime.")
else:
    print("Not prime.")

