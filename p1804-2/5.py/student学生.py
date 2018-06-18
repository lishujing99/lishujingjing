class Student:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.chengjidic={}
    def luchengji(self,xueke,fenshu):
        self.chengjidic[xueke]=fenshu
    def __str__(self):
        return '姓名:%s,性别:%s,年龄:%d,成绩:%s' % (self.name,self.sex,self.age,(self.chengjidic))
huahua=Student('花花','女孩',18)
xiaoxiao=Student('小小','男孩',20)
dongdong=Student('冬冬','男孩',16)
xiaxia=Student('夏夏','女孩',19)
while True:
    print(huahua)
    print(xiaoxiao)
    user=input('输入功能:1开始,8退出')
    if user=='1':
        q=input('输入学科:')
        w=input('输入分数:')
        huahua.luchengji(q,w)
    elif user=='8':
        break
f=open('name.txt','w')
f.write(huahua.__str__())
f.close()
