def add(a,b):
    return a+b

def main():
    print("Welcome")
    print("Invoking from my modules")

#This main() will invoked when we run this module
#It will not get invoke if it used as module
if __name__ == '__main__':
    main()

print("My module to add "+__name__)