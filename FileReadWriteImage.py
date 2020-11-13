"""
This is an document section.This treated as documentations
Not a good way to use multi line comments
"""
try:
    f1 = open("MyPhoto.jpg", "rb")
    f2 = open("MyPic.jpg", "wb")
    for i in f1:
        f2.write(i)
except Exception as e:
    print("Exception occur while read image")
finally:
    f1.close()
    f2.close()

