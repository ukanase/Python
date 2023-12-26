import sys

print(sys.maxsize)  # -> 2^63 - 1
# print(sys.max)

def myPow(x:int):
    print(x)
    print(-x)

myPow(-2147483648)
