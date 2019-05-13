#!/usr/bin/env python3

def max3(a,b,c):
    if a>b:
        # a or c
        if a>c: return a
        else:   return c
    else:
        # b or c
        if b>c: return b
        else:   return c

if __name__=="__main__":
    print("max(1,2,3):",max3(1,2,3))
    print("max(1,3,2):",max3(1,3,2))
    print("max(2,1,3):",max3(2,1,3))
    print("max(2,3,1):",max3(2,3,1))
    print("max(3,1,2):",max3(3,1,2))
    print("max(3,2,1):",max3(3,2,1))

