from array import array

myarray = array("i", [])
n = int(input("Enter the size of array you want"))

for i in range(n):
    val = int(input("Enter your next array value"))
    myarray.append(val)

print(myarray)

search=int(input("enter number to search"))
print("Search using for or while loop")
k=0
for n in myarray:
    if n==search:
        print(k)
        break
    k+=1


print("Search using built function")
print(myarray.index(search))