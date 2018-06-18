# 学生是类 某个学生是对象
class Student:
    def __init__(self,name,age,yuwen,shuxue,english):
        self.name=name
        self.age=age
        self.yuwen=yuwen
        self.shuxue=shuxue
        self.english=english
    def __str__(self):
        q='我的名字是:%s,年龄是:%d,语文成绩是:%d,数学成绩是:%d,英语成绩是:%d' % (self.name,self.age,self.yuwen,self.shuxue,self.english)
        return q
list1=[]
def get1():
    q=input('输入名字：')
    w=int(input('输入年龄：'))
    e=int(input('输入语文成绩：'))
    r=int(input('输入数学成绩：'))
    t=int(input('输入英语成绩：'))
    zt=Student(q,w,e,r,t)
    print(zt)
list1.append(get1)
list1.max(get1)
print(get1)
while True:
    y=input('创建的内容:')
    if y=='1':
        get1()
    else :
        break
