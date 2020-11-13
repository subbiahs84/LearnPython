from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")

t1 = Hello();
t2 = Hi();

t1.start()
t2.start()

#To make main thread to wait until to complete the T1 and T2
t1.join()
t2.join()
print("Bye")