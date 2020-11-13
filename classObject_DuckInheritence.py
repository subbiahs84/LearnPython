
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("spell Check")
        print("Spell check completed")

class Laptop:
    def code(self, ide):
        ide.execute()

idepycharm=Pycharm()
idemyedit=MyEditor()

lap1 = Laptop()
lap1.code(idemyedit)
lap1.code(idepycharm)

