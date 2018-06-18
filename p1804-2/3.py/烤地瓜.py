# 烤地瓜，对象 ，类，
# 对象： 每一个烤熟的地瓜都是
# 过程： 烤地瓜的过程

class Digua:
    def __init__(self):
        self.info='生地瓜'
        self.time1=0
        self.tiaoliao1=[]
    def kao(self,t):
        self.time1=self.time1+t
        if self.time1>=8:
            self.info='烤糊了的地瓜'
        elif self.time1>=6:
            self.info='火大的地瓜'
        elif self.time1==5:
            self.info='刚刚好的地瓜'
        elif self.time1>=3:
            self.info='半生不熟的地瓜'
        else:
            self.info='生地瓜'
    def tiaoliao(self,add):
        self.tiaoliao1.append(add)
        for i in self.tiaoliao1:
            self.info=self.info+i+','
            self.info=self.info.strip(',')



    def __str__(self):
        return '当前的地瓜状态是:%s,烤的时间是:%s,' % (self.info,self.time1)
dg1=Digua()
 #dg1.tiaoliao('蜂蜜')
print(dg1.info)
dg1.kao(5)
dg1.tiaoliao('哈密瓜糖')
print(dg1.info)
print(dg1)

