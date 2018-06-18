class Car:
    def __init__(self,name,lunzi,color):
        self.name=name
        self.lunzi=lunzi
        self.color=color
    def pao(self):
        print(' %s汽车跑起来了......' % self.name)
    def jiao(self):
        print(' %s汽车急不可耐喇叫起来了......' % self.name)
    def zhui(self):
        print('%s汽车追尾了......' % self.name)
    def introduce(self):
        print('我的名字是%s,我的颜色是%s，我有%s个轮子' % (self.name,self.color,self.lunzi))
    def __str__(self):
        return 'hihihi'
baoma=Car('宝马','4','黑色')
print('nini ' , baoma)
baoma.introduce()
baoma.pao()
fute=Car('福特','3','白色')
print('哈喽', fute)
fute.introduce()
fute.pao()
fute.zhui()
aodi=Car('奥迪','6','红色')
print('嗨', aodi)
aodi.introduce()
aodi.jiao()
zhangting=Car('张婷','2','黑色')
zhangting.introduce()
zhangting.jiao()
zhangting.zhui()



