from builtins import print

from numpy import *
arr1 = array([
    [1,2,3,4,5],
    [6,7,8,9,10]

])

m = matrix(arr1)

print(arr1)
print(arr1.dtype)
print(arr1.ndim)

print(arr1.flatten())