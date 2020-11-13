from numpy import *

arr = array([23,34,45,6,10,5])
print(arr.dtype)
arr = arr+3
print(arr)

arr = linspace(0, 10, 10)
print(arr)

arr = arange(1,10,2)
print(arr)


print("Add two arrays")
arr1 = array([1,2,3,4,5])
arr2 = array([9,8,7,6,5])
arr3 = arr1+arr2
print(arr3)
print(sum(arr3))

print(concatenate(arr1,arr2))