class Car(object):
    def __init__(self,name):
        self.name=name
    def feiben(self):
        return '汽车飞奔---'
class Dazhong(Car):
    def feiben(self):
        return '大众汽车飞奔 @ @ @'
class Baoma(Car):
    def feiben(self):
        return '宝马汽车飞奔！！！'
class Benchi(Car):
    def feiben(self):
        return '奔驰汽车飞奔# # #'
class People(object):
    def __init__(self,xingming):
        self.xingming=xingming
    def kaiche(self,che):
        print(' %s在%s' % (self.xingming,che.feiben()) )
    def paoniu(self,qiche):
        print('%s开%s去泡妞' % (self.xingming,qiche.feiben()))
xiaoche=Car('小车')
dzc=Dazhong('大众汽车')
bm=Baoma('宝马汽车')
bc=Benchi('奔驰汽车')
tiantian=People('笑笑')
tiantian.kaiche(xiaoche)
xiaoxiao=People('小小')
xiaoxiao.kaiche(dzc)
mingming=People('明明')
mingming.kaiche(bm)
honghong=People('红红')
honghong.kaiche(bc)
tiantian.paoniu(bm)




