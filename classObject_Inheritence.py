class A:

    def __init__(self):
        print("A init constructor")

    def feature1(self):
        print("Class A Feature - 1")

    def feature2(self):
        print("Class A Feature - 2 ")

#Single Level Inheritence
class B (A) :

    def __init__(self):
        super().__init__()
        print("B init constructor")

    def feature3(self):
        print("Class B Feature - 3")

    def feature4(self):
        print("Class B Feature - 4")


a = B()
