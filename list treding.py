'''import threading
import time
class ThreadingExample(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("process"+str(i))
            time.sleep(1)
obj=ThreadingExample()
obj.start()
obj.join()
obj1=ThreadingExample()
obj1.start()
obj1.join()
obj2=ThreadingExample()
obj2.start()
obj.join()'''
###how to implement thread for procedural programming
'''import time
import threading

def fun():
    for i in range(1,10):
        print(i)
        time.sleep(1)
t1=threading.Thread(target=fun)
t1.start()
t1.join()
t2=threading.Thread(target=fun)
t2.start()
o/p-:[1,2,3,4,5,6,7,8,9]
import threading
import time
class ThreadExample(threading.Thread):
    def run(self):
        for i in range(1,10):
         print("process"+str(i))
         time.sleep(1)
t1=ThreadExample()
t1.start()
t1.join()
t2=ThreadExample()
t2.start()

import threading
import time
class Thread1(threading.Thread):
  def __init__(self):
    super(Thread1,self).__init__()
    self.num=int(input("enter number"))
  def run(self):
    for i in range(1,11):
      print(self.num*i)
      time.sleep(1)

class Thread2(Thread1):
    def __init__(self):
      super(Thread2,self).__init__()
    def run(self):
      self.s='  '
      self.fect=1
      for i in range(self.num,0,-1):
        self.s=self.s+str(i)+"*"
        self.fect=self.fect*i
        time.sleep(1)
        print("result is"+self.s+"="+str(self.fect))
t1=Thread1()
t1.start()
t1.join()
t2=Thread2()
t2.start()
#output-:
 # 5,10,15,20,25,30,35,40,45,50
  result is  5*=5
result is  5*4*=20
result is  5*4*3*=60
result is  5*4*3*2*=120
result is  5*4*3*2*1*=120
 ##how to implement thread for procedural programming?
import time
import threading
def fun():
 for i in range(1,10):
  print(i)
  time.sleep(1)
t1=threading.Thread(target=fun)
t1.start()
t1.join()
t2=threading.Thread(target=fun)
t2.start()
output:-
 1,2,3,4,5,6,7,8,9,10
###wap to thread to calculate table using class-based and method based program
import threading
import time
class Table(threading.Thread):
  def __init__(self,num):
    super().__init__()
    self.num=num
  def run(self):
    for i in range(1,11):
      print(str(self.num*i)+" ")
      time.sleep(1)
t=Table(5)
t.start()
t.join()
t1=Table(9)
t1.start()
output:-
5,10,15,20,25,30,35,40,45,50
9,18,27,36,45,54,63,72,81,90
#method based program
import threading
import time
def table(num):
  for i in range(1,11):
    print(str(num*i)+"")
    time.sleep(1)

    
t=threading.Thread(target=table(5))
t.start()
t1=threading.Thread(target=table(9))
t1.start()
output:-
5,10,15,20,25,30,35,40,45,50
9,18,27,36,45,54,63,72,81,90'''

import threading
import time
from random import randint

class SharedCounter(object):

  def __init__(self,val=0):
    self.lock=threading.Lock()
    self.counter=val
  def increment(self):
   print("waiting\n")
   self.lock.acquire()
   try:
     print("acquired",self.counter,"\n")
     self.counter=self.counter+1
   finally:
     print("Released a lock,counter value:',self.counter")
     self.lock.release()
def xyz(c):
    r=randint(1,5)
    for i in range(r):
      c.increment()
      print("done")

sCounter=SharedCounter()
t1=threading.Thread(target=xyz,args=(sCounter,))
t1.start()
output:-
waiting

acquired 0 

Released a lock,counter value:',self.counter
done
waiting

acquired 1 

Released a lock,counter value:',self.counter
done
waiting

acquired 2 

Released a lock,counter value:',self.counter
done











