def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

n = int(input("Enter the number to get factorial-"))
factValue = fact(n)
print("Using FOR loop, Factorial value for the {} is {}".format(n, factValue))

#Factorial using recursion

def factRecursion(n):
    if(n==0):
        return 1
    return n*factRecursion(n-1)
result = factRecursion(n)
print("Factorial using recursion - ", result)

