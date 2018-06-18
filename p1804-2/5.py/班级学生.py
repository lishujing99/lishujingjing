class Banjilei:
    def __init__(self,teacher,bjname,stulist):
        self.teacher=teacher
        self.bjname=bjname
        self.stulist=[]
class Studentlei(Banjilei):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.chengjidic={}
class Chengjilei(Studentlei):
    def __init__(self,yuwen,shuxue,yingyu):
        self.yuwen=yuwen
        self.shuxue=shuxue
        self.yingyu=yingyu
    def get_chengji(self.choose):
        self.chengjidic['语文']=self.yuwen
        self.chengjidic['数学']=self.shuxue
        self.chengjidic['英语']=self.yingyu
tiantian=Studentlei('天天',16,'女孩')




