 # KFC
kfclist=[]
def kfc():
    print('欢迎光临KFC')
    print('1,光临人数:')
    print('2,美食汉堡/卷')
    print('3,小食配餐')
    print('4,缤纷饮料')
    print('5,甜品，冰淇淋')
    print('6,欢乐套餐')
    print('7,结帐')
kfc()
def renshu():
    yy=int(input('请问是几位?'))
    if yy==1:
        print('请坐两人桌')
    elif yy==2:
        print('请坐两人桌')
    elif yy==3:
        print('请坐四人桌')
    elif yy==4:
        print('请坐四人桌')
    else:
        print('请坐')
def meishi():
    print('至尊虾堡,香辣鸡腿堡,新奥尔良烤鸡腿堡')
    print('老北京鸡肉卷，牛肉卷')
    xx=input('请问吃什么? 什么口味?')
    dic1={}
    dic1['吃什么:']= xx
    kfclist.append(dic1)
    for i in kfclist:
        print(kfclist)
def xiaoshi():
    print('薯条,鸡米花,爆米花')
    ee=input('请问吃什么')
    dic2={}
    dic2['吃什么:']=ee
    kfclist.append(dic2)
def yinliao():
    print('可乐，雪碧，果汁，咖啡')
    rr=input('请问需要喝什么')
    dic3={}
    dic3['喝什么:']=rr
    kfclist.append(dic3)
def tianpin():
    print('圣代，冰淇淋，蛋挞')
    ww=input('请问吃什么?')
    dic4={}
    dic4['吃什么:']= ww
    kfclist.append(dic4)
    print(kfclist)
def taocan():
    print('卷堡三人餐')
    print('鸡翅堡二人餐')
    print('汉堡多人餐')
    tt=input('请问吃什么')
    dic5={}
    dic5['吃什么:']= tt
    kfclist.append(dic5)
    print(kfclist)
def jiezhang():
    print('你好你一共消费:')
    len(kfclist)
    print(kfclist)
while True:
    user=input('请输入数字:')
    if user=='1':
        renshu()
    elif user=='2':
        m'eishi()
    elif user=='3':
        xiaoshi()
    elif user=='4':
        yinliao()
    elif user=='5':
        tianpin()
    elif user=='6':
        taocan()
    elif user=='7':
        break







