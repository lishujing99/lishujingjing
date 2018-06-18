class Animal:
    def __init__(self):
        self.__name='动物'
    def get(self):
        return self.__name
    def gai(self):
        return self.__name='huahua'
    def eat(self):
        print('%s吃东西' % self.name)
    def drink(self):
        print('%s喝可乐' % self.name)
    def sleep(self):
        print('%s睡觉' % self.name)
class Dog(Animal):
    def jiao(self):
        print('旺旺旺旺')
class Cat(Dog):
    pass
#dagou=Animal('大狗')
#dagou.eat()
#xiaogou=Dog('小狗')
#o96xiaogou.eat()
#xiaomao=Cat('小猫')
#xiaomao.drink()
xiaomao=Cat()
aa=xiaomao.get()
print(aa)
