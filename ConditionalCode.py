n=6
if n < 5 :
    print("Number is less than 5")
elif n < 10 :
    print("Number is less than 10 greater 5 ")
else:
    print("Number is greater")

i=1
while i<=5:
    print("While loop ", i)
    i += 1

li = ['Subbiah', 1984, "GlobalLogic", 12345.65]
for x in li:
    print(x)

for i in range(5):
    print(i)

for j in range(1,20,2):
    if j==11:
        break
    print(j)

for i in range(10):
    if(i%3==0):
        continue
    print(i)

for i in range(4):
    for j in range(4):
        print("#" , end = ' ')
    print()

nums = [20,5,32,36,7]
for num in nums:
    if num % 8 == 0 :
        print(num)
        break
else:
    print("Unable to find any number which was divise by 8")

import array as arr
print("To create an integer array")
vals = arr.array('i',[23,3,4,5,6])
print(vals)
print(vals.buffer_info())

print("Copy array value")
vals = arr.array('i',[23,3,4,5,6])
newArr = arr.array(vals.typecode, (a for a in vals))
print("Copied array value")
for e in newArr:
    print(e)
