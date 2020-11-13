class Computer:

    def __init__(self):
        self.RAM = "4GB"
        self.CPU = "i3"

    def config(self, name):
        print("{}  Computer configuration RAM - {} CPU {} -".format(name,self.RAM, self.CPU))

    def update(selfself):
        selfself.RAM="32GB"

    def compare(self, anotherObj):
        if(self.RAM==anotherObj.RAM):
            return True
        else:
            return False

com1 = Computer()
com1.RAM="10GB"
Computer.config(com1, "Subbiah")

com2 = Computer()
com2.RAM="10GB"
com2.config("Sankaralingam")

print(com1.compare(com2))

