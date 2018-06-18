#对象是：烤好的每一个鸡翅
class Jc:
    def __init__(self):
        self.info='生鸡翅'
        self.time1=0
        self.tiaoliao1=[]
    def kao(self,t):
        self.time1=self.time1+t
        if self.time1>=25:
            self.info='烤糊了黑鸡翅'
        elif self.time1>=20:
            self.info='火大的半黑鸡翅'
        elif self.time1>=15:
            self.info='刚刚好的好鸡翅'
        elif self.time1>=10:
            self.info='半生不熟的鸡翅'
        else:
            self.info='生鸡翅'
    def tiaoliao(self,tltype):
        self.tiaoliao1.append(tltype)

    def __str__(self):
        tl=''
        for i in self.tiaoliao1:
            tl=tl+i+','
        tl='调料:'+tl
        tl=tl.strip(',')
        return '当前的鸡翅状态是: %s,时间是:%d %s' % (self.info,self.time1,tl)
jichi=Jc()
while True:
    q=input('时间')
    if q=='q':
        break
    q=int(q)
    jichi.kao(q)
    w=input('调料')
    jichi.tiaoliao(w)
     #print(jichi.info)
    print(jichi)


