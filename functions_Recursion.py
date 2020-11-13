import sys

print(sys.getrecursionlimit())
#Override the default recursion Limi
sys.setrecursionlimit(100)

def recur():
    print("Hi Hello")
    recur()

recur()