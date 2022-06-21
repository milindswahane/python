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
     print("Acquired",self.counter,"\n")
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
