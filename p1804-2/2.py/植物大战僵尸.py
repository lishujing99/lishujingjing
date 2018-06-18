class Zhiwu:
    def __init__(self,name,color,dh):
        self.name=name
        self.color=color
        self.dh=dh
    def sun(self):
        print('%s放阳光......' % self.name)
    def yaotou(self):
        print('%s摇头......' % self.name)
    def fapao(self):
        print('发炮......')
    def zudang(self):
        print('阻挡zhong......')
    def __str__(self):
        q='我的名字是:'+self.name +'**我的颜色是:' + self.color  + '**我的血型是:'+self.dh
        return q
def zuhe(object1):
    object1.sun()
    object1.yaotou()
xrk=Zhiwu('向日葵','黄色','100')
print(xrk)
#xrk.sun()
#xrk.yaotou()
zuhe(xrk)
wd=Zhiwu('豌豆','绿色','99')
# print(wd)
# wd.yaotou()
# wd.fapao()
jg=Zhiwu('坚果','土色','95')
# print(jg)
# wd.zudang()

class Js:
    def __init__(self,name,color,dh):
        self.name=name
        self.color=color
        self.dh=dh
    def jump(self):
        print('%s僵尸跳跳......' % self.name)
    def eat(self):
        print('%s僵尸吃吃......' % self.name)
    def tang(self):
        print('%s僵尸躺下去世' % self.name)
    def __str__(self):
        q='我的名字是:'+ self.name+'**我的颜色是:'+self.color
        return q
def zuhe(object2):
    object2.jump()
    object2.eat()
    object2.tang()
xiaolv=Js('小绿','绿色','80')
print(xiaolv)
zuhe(xiaolv)

