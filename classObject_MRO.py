class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")

c = C()
print(C.mro())