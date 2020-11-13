
f = open("MyData", "r")

#Copy the file from one to another

f1 = open("SubbiahData", "w")
for obj in f:
    f1.write(obj)
f1.close();

f2 = open("SubbiahData", "r")
print(f2.read())