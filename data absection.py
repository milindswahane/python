'''from abc import ABC,abstractmethod
class Area (ABC):
    @abstractmethod
    def triangal(self):
        pass
    @abstractmethod
    def rectangle(self):
        pass
class Createarea(Area):
    def triangal(self):
        print("triangal")
    def rectangle(self):
        print("rectangle")
    def fun(self):
        pass

obj=Createarea()
obj.triangal()
obj.rectangle()'''

from abc import ABC,abstractmethod
class Smartphone(ABC):
    @abstractmethod
    def screen(self):
        pass
    @abstractmethod
    def multimedia(self):
        pass
    @abstractmethod
    def software(self):
        pass
    @abstractmethod
    def hardware(self):
        pass

class Androidphone(Smartphone):
    def screen(self):
        print("screen size")

    def multimedia(self):
        print("multimedia")
    def software(self):
        print("nougat")
    def hardware(self):
        print("hardware")
        
class AndroidphoneNew(Androidphone):
    def screen(self):
        print("new Screen")
    def software(self):
        print("orio")  








        
