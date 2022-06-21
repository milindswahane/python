'''import threading
import time
class ThreadExample(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("procces"+str(i))
            time.sleep(1)

obj=ThreadExample()
obj.start()

obj1=ThreadExample()
obj1.start()

obj1=ThreadExample()
obj1.start() 
import threading
import time
class ThareadExample(threading.Thread):
    def run(self):
        for i in range(1,10):
            print("process is"+str(i))
            time.sleep(1)
obj=ThreadExample()
obj.start()

obj1=ThreadExample()
obj1.start()
obj2=ThreadExample()
obj2.start()

import threading
import time
class ThreadExample(threading.Thread):
    def run(self):
        for i in range(1,10):
            print("process is",str(i))
            time.sleep(1)
            
obj=ThreadExample()
obj.start()
obj1=ThreadExample()
obj1.start()

obj2=ThreadExample()
obj2.start()  
import threading
import time
class ThreadExample(threading.Thread):
    def run(self):
        for i in range(1,10):
            print("process is "+str(i))
            time.sleep(1)


t1=ThreadExample()
t1.start()
t1.join()
t2=ThreadExample()
t2.start()
t2.join()
t3=ThreadExample()
t3.start() 
import threading
import time
class Thread1(threading.Thread):
    def __init__(self):
        super(Thread1, self).__init__()
        self.num=int(input("enter number"))
    def run(self):
        for i in range(1,11):
            print(self.num*i)
            time.sleep(1)
class Thread2(Thread1):
    def __init__(self):
        super(Thread2,self).__init__()
    def run(self):
        self.s=""
        self.fact=1
        for i in range(self.num,0,-1):
            self.s=self.s+str(i)+"*"
            self.fact=self.fact*i
            time.sleep(1)
        print("result is"+self.s+"="+str(self.fact))
t1=Thread1()
t1.start()
t1.join()
t2=Thread2()
t2.start()
'''
import random
while True:
    print(random.randint(1,6))
roll = input("Want to roll the dice again ? (y/n)")
if roll.lower()== "y":
    continue
else:
    break




