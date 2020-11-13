from array import array

numArray = array("i", [])
n = int(input("Enter the number of elements "))

for i in range(n):
    value = int(input("Enter the array value "))
    numArray.append(value)

def countEvenOdd(numList):
    odd = 0
    even = 0

    for n in numList:
        if n%2==0:
            odd+=1
        else:
            even+=1
    return odd, even

odd, even = countEvenOdd(numArray)

print("Number of odd - {}, even - {}".format(odd,even))