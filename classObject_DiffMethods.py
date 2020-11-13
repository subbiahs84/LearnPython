class student:

    school = "St.Johns HSS"

#Default constructors
    def __init__(self, m1, m2 ,m3):
        self.m1=m1
        self.m2 = m2
        self.m3 = m3

##Instnace methods
  #Accessor Methods
    def get_m1(self):
        return self.m1

  #Mutator methods
    def set_m1(self, m1):
        self.m1 = m1;

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchoolName(cls):
        return cls.school

    @staticmethod
    def getInfo():
        print("This class about the student class")

s1 = student(75,85,80)
print(s1.m1, s1.m2, s1.m3)

print(s1.get_m1())

print("Average marks - ",s1.avg())
print("Better school - ",student.getSchoolName())

student.getInfo()