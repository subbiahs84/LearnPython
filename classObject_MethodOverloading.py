
class Student:
    def sum(self, a=None, b=None, c=None):
        s = 0;
        if(a != None and b!= None and c!=None):
            s=a+b+c
        elif(a!= None and b!=None):
            s=a+b
        elif(a!=None):
            s=a

        return s
student = Student()
total = student.sum()
print(total)

total1 = student.sum(10)
print(total1)

total2 = student.sum(10,20)
print(total2)

total3 = student.sum(10,20,30)
print(total3)
