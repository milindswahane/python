'''###super key word in pythen

class A:
    def display(self):
        print("A")
class B(A):
    def display1(self):
        super().display()
        print("B")
obj=B()
obj.display1()
output:-
A,B
 ###wap to init methde in super key
class main:
    def fun(self):
        print("main")

class A(main):
    def __init__(self):
        print("A INIT")
    def display(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print("B INIT")
    def display1(self):
        super().fun()
        super().display()
        print("B")
obj=B()
obj.display1()
#output:-A INIT
B INIT
main
A
B'''



















