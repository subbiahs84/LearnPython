from builtins import print


def myFunction():
    print("Hello")
    print("Welcome to python function")

myFunction()

def add(x,y):
    c=x+y
    print(c)
    return c

result = add(10,20)
print(result)

def add_sub(x,y):
    a=x+y
    s=x-y
    return a,s

result = add_sub(20,10)
print(result[1])

result1,result2 = add_sub(50,25)


def updateValue(x):
    print("X address before update - ",id(x))
    print("x = ", x)
    x = 10
    print("X address after update - ", id(x))
    print("x = ",x)

a  = 15
print("A address before invoke update by param of a address - ",id(a))
updateValue(id(a))
print("a address after update-",id(a))
print("a = ", a)

def updateList(list):
    print("List param address -",id(list))
    list[1]=25
    print(list)
myList=[10,20,30]
print("My list address - ",id(myList))
updateList(myList)
print(myList)

def person(name, age):
    print("Name - ",name)
    print("Age - ",age)

person(23,"subbiah")
person(age=23, name="Subbiah Sankar")

def person(name, age=25):
    print("Name - ",name)
    print("Age - ",age)

person(23,"subbiah")
person(name="Subbiah Sankar")

def sum(a, *b):
    print("a=", a)
    print("Tuple b =", b)
    c=a
    for i in b:
        c=c+i
    print(c)
print("Variable length arguments")
sum(10,20,21,5,6)

def person(name, **data):
    print("Name - ", name)
    for i,j in data.items():
        print(i,j)
person("Subbiah", age=25, City="Nellai", Mobile=96770)

##comment1
a = 10
def globaFun():
    global a
    a=15
    print("Inside the function a=",a)

globaFun()
print("Outside function a = ", a)

## access global variable using globals()
x = 12
print("Memory address of X-",id(x))
def globalFunc():
    x = 15
    print("Local variable x=",x)
    y = globals()['x']
    print("y=",y)
    print("Memory address of y-",id(y))
globalFunc()