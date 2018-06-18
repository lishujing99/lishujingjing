import sys
class People:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Worder:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
tiantian=People('天天',6000)
tiantian1=tiantian
tiantian2=tiantian
print(sys.getrefcount(tiantian))
print(isinstance(tiantian,People))
