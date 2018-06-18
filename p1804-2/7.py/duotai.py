class Duck(object):
    def walk(self):
        print('小黄鸭子在散步')
    def swim(self):
        print('小黄鸭子在游泳')
class People(object):
    def walk(self):
        print('老王在散步')
    def swim(self):
        print('老王在游泳')
def Func(obj):
    obj.walk()
    obj.swim()

duck=Duck()
p01=People()
Func(duck)
Func(p01)


