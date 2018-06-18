# 类： 房子类  家具类
class House:
    def __init__(self,area,address):
        self.area=area
        self.address=address
        self.jiajulist=[]
    def addjiaju(self,jiaju):
        if int(self.area) > int(jiaju.area1): # 如果房子的面积大于家具的面积就加
            self.area=int(self.area)-int(jiaju.area1)
            self.jiajulist.append(jiaju.name)
        else:
            print('家具太大了！！！')
    def get_area(self,shenf):
        if shenf=='老妈':
            print(house1)
        else:
            print('啥也没有`')
    def __str__(self):
        return '%s 已经买好了，地址位于%s,里面有一个%s' % (self.area,self.address,self.jiajulist)
class Bed:
    def __init__(self,area1,name):
        self.area1=area1
        self.name=name
    def __str__(self):
        return '%s 已经买好了，大小是:%s' % (self.name,self.area1)
house1=House(3000,'老街16号')
#print(house1)
babybed=Bed(100,'宝宝床')
#print(babybed)
sofa=Bed(300,'沙发')
#print(babybed)
house1.addjiaju(babybed)
house1.addjiaju(sofa)
#print(house1)
while True:
    a=input('输入身份:')
    house1.get_area(a)
    if a=='q':
        break

