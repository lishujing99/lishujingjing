class Cat(object):
    def __init__(self,name):
        self.name=name
        self.color='yellow'
class Bosi(Cat):
    def __init__(self,name):
        #Cat.__init__(self,name)
        #super(Bosi,self).__init__(name)
        super().__init__(name)
    def getname(self):
        return self.name
bosi=Bosi('小花')
print(bosi.name)
print(bosi.color)
