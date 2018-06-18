class Banjilei:
    def __init__(self,banzhuren,banjihao):
        self.banzhuren=banzhuren
        self.banjihao=banjihao
        self.studentlist=[]
    def addinfo2(self):
        self.studentlist.append(self.banzhuren)
        self.studentlist.append(self.banjihao)
    def __str__(self):
        return '班主任是:%s 班级编号:%s' % (self.banzhuren,self.banjihao)
class Studentlei(Banjilei):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.xueshengdic={}
    def addinfo(self):
        self.xueshengdic['姓名']=self.name
        self.xueshengdic['年龄']=self.age
        self.xueshengdic['性别']=self.sex
    def __str__(self):
        return '学生名字是:%s,年龄是:%s,性别是:%s' % (self.name,self.age,self.sex)
class Chengjilei(Studentlei):
    def __init__(self,yuwen,shuxue,yingyu):
        self.yuwen=yuwen
        self.shuxue=shuxue
        self.yingyu=yingyu
        self.chengjidic={}
    def addinfo1(self):
        self.chengjidic['语文']=self.yuwen
        self.chengjidic['数学']=self.shuxue
        self.chengjidic['英语']=self.yingyu
    def get_info(self,chaxun):
        if chaxun==q:
            return self.studentlist
    #def xiugai_info(self,xiugai):
     #   if xiugai==a:
      #      d=input('修改的语文分数')
       #     return self.chengjidic['语文']=d

    def __str__(self):
        return '语文成绩是:%s,数学成绩是:%s,英语成绩是:%s' % (self.yuwen,self.shuxue,self.yingyu)
q=input('请输入班主任名字:')
w=input('请输入班级编号:')
q=Banjilei(q,w)
q.addinfo2()
print(q.studentlist)
print(q)



while True:
    user=input('功能:[1,添加;2,查询;8,退出;]')
    if user=='8':
        break
    elif user=='1':
        e=input('请输入名字:')
        r=input('请输入年龄:')
        t=input('请输入性别:')
        e=Studentlei(e,r,t)
        e.addinfo()
        print(e.xueshengdic)
        print(e)

        u=input('语文成绩是:')
        i=input('数学成绩是:')
        o=input('英语成绩是:')
        u=Chengjilei(u,i,o)
        u.addinfo1()
        print(u.chengjidic)
        print(o)
        e.xueshengdic.update(u.chengjidic)
        #print(e.xueshengdic)
        q.studentlist.append(e.xueshengdic)
        print(q.studentlist)

    elif user=='2':
        p=input('请输入查询的名字:')
        u.get_info(p)
        print(u)

