'''class Student:
    def accept(self,rno,name):
        self.rno=rno
        self.name=name
    def display(self):
        print("rno is",self.rno,"name is",self.name)


obj=Student()
obj.accept(85,"ram")
obj.display()
obj=Student()
obj.accept(46,"anup")
obj.display()  
class Student:
    def accept(self):
        self.rno=45
        self.name="ram"
        self.rno=58
        self.name="rajesh"
        
    def display(self):
        print("rno is",self.rno,"name is",self.name)


obj=Student()
obj.accept()
obj.display()
obj1=Student()
obj1.accept()
obj1.display()
class SI:
    def accept(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t
    def logic(self):
        self.SI=(self.p*self.r*self.t)/100
    def display(self):
        print("result is"+str(self.SI))
obj=SI()
obj.accept(5000,2,2)
obj.logic()
obj.display()'''
class SI:
    def accept(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t
    def logic(self):
        self.SI=(self.p*self.r*self.t)/100
    def display(self):
        print("result is"+str(self.SI))
ob=[]
for i in range(0,2):
    obj=SI()
    obj.accept(5000,2,2)
    obj.logic()
    ob.append(obj)
for i in range(0,2):
    ob[i].display()



