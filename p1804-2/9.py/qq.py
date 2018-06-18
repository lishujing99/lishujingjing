
namelist=[]
def mingpian():
    print('*'*30)
    print('1,开始创建名片')
    print('2,查询名片')
    print('3,删除名片')
    print('4,退出编辑')
    print('5,添加名片')
    print('*'*30)
mingpian()
def xinjian():
    print('开始新建名片^8^')
    name=input('请输入名字:')
    com=input('请输入公司:')
    sex=input('请输入性别:')
    phone=input('请输入联系方式:')
    dic={'姓名':name,'公司':com,'性别':sex,'联系方式':phone}
    namelist.append(dic)
    print(namelist)
def chaxun():
    print('开始查询名片')
    qq=int(input('请问你想查看第几张名片?'))
    qq=qq-1
    print(namelist[qq])
    print(qq)
def shanchu():
    ww=int(input('请问需要删除第几张名片?'))
    del namelist[ww]
    print(namelist)
    print(ww)
def tuichu():
    print('如需退出输入q')
def charu():
    yy=int(input('请输入要插入的下标位置:'))
    xx=input('请问输入需要插入的内容?')
    yy=yy-1
    namelist.insert(yy,xx)
    print(namelist)
while True:
    user=input('请输入数字')
    if user=='1':
        xinjian()
    elif user=='2':
        chaxun()
    elif user=='3':
        shanchu()
    elif user=='4':
        break
    elif user=='6':
        charu()
