
a=10

try:
    b = int(input("Enter the number to divide"))
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("The number cannot be divide by ZERO")
except ValueError as e:
    print("Input number is invalid")
except Exception as e:
    print("Inside the catch block in Exception")
    print(e)

finally:
    print("Inside the finally block")
print("End")