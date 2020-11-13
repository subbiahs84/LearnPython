
def printFib(n):
    a = 0
    b = 1
    print(a, b)
    for i in range(2,n):
        c = a+b
        a=b
        b=c
        print(c)

n =  int(input("Enter number of Fibonacci series"))
printFib(n)