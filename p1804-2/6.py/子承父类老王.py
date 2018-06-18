class Father(object):
    def __init__(self,sex,sex1,sex2):
        self.sex=sex
        self.sex1=sex1
        self.sex2=sex2
        self.__shengao='160'
    def kaiche(self):
        print('天生会开车.')
    def __dubo(self):
        print('赌博赖账，卖儿子')
class Son(Father):
    def __init__(self,na,name,name1,name2):
        self.ming=name1
        #super().__init__(name)
        #Father.__init__(self.name)
        super(Son,self).__init__(name,na,name2)
    def kaiche(self):
        print('赛车天生会开')
        super().kaiche()
xiaoming=Son('男','女','小孩','大人')
print(xiaoming.sex)
print(xiaoming.sex1)
print(xiaoming.ming)
print(xiaoming.sex2)


