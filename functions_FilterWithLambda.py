from functools import reduce
nums = [12,13,15,16,20,25]

evenResult = list(filter(lambda n : n % 2 == 0, nums))
print("Even result from List ",evenResult)

mapResult = list(map(lambda n: n*2, evenResult))
print("Map result - ", mapResult)

sum = reduce(lambda a,b : a+b, evenResult)
print("Calculate SUM using reduce ", sum)