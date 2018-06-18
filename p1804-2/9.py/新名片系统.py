
namelist=[]
class Pian(object):
    def mingpian(self):
        print('*'*30)
        print('1,查看目录')
        print('2,开始创建名片')
        print('3,查询名片')
        print('4,删除名片')
        print('8,退出编辑')
        print('5,添加名片')
        print('*'*30)
    def xinjian(self):
        print('开始新建名片^8^')
        name=input('请输入名字:')
        com=input('请输入公司:')
        sex=input('请输入性别:')
        phone=input('请输入联系方式:')
        dic={'姓名':name,'公司':com,'性别':sex,'联系方式':phone}
        namelist.append(dic)
        print(namelist)
    def chaxun(self):
        print('开始查询名片')
        qq=int(input('请问你想查看第几张名片?'))
        qq=qq-1
        print(namelist[qq])
        print(qq)
    def shanchu(self):
        ww=int(input('请问需要删除第几张名片?'))
        del namelist[ww]
        print(namelist)
        print(ww)
    def tuichu(self):
        print('如需退出输入q')
    def charu(self):
        yy=int(input('请输入要插入的下标位置:'))
        xx=input('请问输入需要插入的内容?')
        yy=yy-1
        namelist.insert(yy,xx)
        print(namelist)
    def fangfa(self):
        while True:
            user=input('请输入数字')
            if user=='1':
                self.mingpian()
            elif user=='2':
                self.xinjian()
            elif user=='3':
                self.chaxun()
            elif user=='4':
                self.shanchu()
            elif user=='8':
                break
            elif user=='5':
                self.charu()
class Ming(Pian):
    __instance=None
    __first_init=False
    def __new__(cls,mingzi):
        if cls.__instance==None:
            cls.__instance=super().__new__(cls)
        return cls.__instance
    def __init__(self,name):
        if self.__first_init==False:
            self.name=name
            Ming.__first_init=True

mingpian=Ming('名片系统')
mingpian.fangfa()
