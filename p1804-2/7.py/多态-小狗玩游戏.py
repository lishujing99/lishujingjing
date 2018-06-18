
class Dog(object):
    def __init__(self,xingming):
        self.xingming=xingming
    def game1(self):
        return '普通狗狗只是简单的玩耍'
class Xdog(Dog):
    def game1(self):
        return '小天犬需要在天上玩耍'

class People(object):
    def __init__(self,name):
        self.name=name
    def play_dog(self,dog):
        print('%s在和%s' % (self.name,dog.game1()))
w=input('输入狗:')
xg=Xdog(w)
q=input('输入人:')
p=People(q)
p.play_dog(xg)


