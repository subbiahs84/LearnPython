from builtins import print

a = 5
b = 6
c='Subbiah'

print(a+b)
#print(a+c)

print(int.__add__(a,b))
#int.__add__(a,c) unsupported operand type(s) for +: 'int' and 'str'

class student:
    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1+self.m2
        r2 = other.m1+other.m2
        if r1 > r2:
            return True
        else:
            return False

    #This will return tuple
    def __str__(self):
        return self.m1, self.m2

    #this will return String
    def __str__(self):
        return '{}, {}'.format(self.m1, self.m2)

s1 = student(75, 81)
s2  = student(80,75)

#will invoke operator overload __add__
s3 = s1+s2
print(s3.m1)
print(s3.m2)

#will invoke the operator overload __gt__
if(s1>s2):
    print("S1 Wins")
else:
    print("S2 wins")

print(s2)
print(s1.__str__())


