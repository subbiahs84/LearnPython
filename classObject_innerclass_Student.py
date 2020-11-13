class Student:
    def __init__(self, id, name, dept, model):
        self.id=id
        self.name=name
        self.dept = dept
        self.lab= self.Laptop(model, "16GB")

    def show(self):
        print(self.id,self.name, self.dept)
        self.lab.show()

#Inner class
    class Laptop:
        def __init__(self, model, ramSize):
            self.model= model
            self.ramSize=ramSize

        def show(self):
            print(self.model, self.ramSize)

s1 = Student(4944, "Kaavya", "CSE", "HP")
s2 = Student(9677, "Subbiah", "IT", "DELL")

s1.show()
s2.show()
lab1 = s1.Laptop
lab2 = s2.Laptop

print(id(lab1))
print(id(lab2))
