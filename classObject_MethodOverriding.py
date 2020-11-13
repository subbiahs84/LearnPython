class A:
    def show(self):
        print("In A show")

class B(A):
    def show(self):
        print("In B show")

a = A()
a.show();

b = B()
b.show()

nums = [23,4,5,3,]
it = iter(nums)
print(it.__next__())
print(it.__next__())
print("After next()")
for i in it:
    print(i)