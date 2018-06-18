class Duck():
    def eat(self):
        print('嘎嘎喜欢吃橙子')
    def swim(self):
        print('嘎嘎喜欢游泳')
class Daduck():
    def eat(self):
        print('大鸭子喜欢吃苹果')
    def swim(self):
        print('大鸭子喜欢浮水')
class People(object):
    pass
    def func(obj,yazi):
        return yazi.swim()
p01=People()
xiaohua=Duck()
p01.func(xiaohua)

