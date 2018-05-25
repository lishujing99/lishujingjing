kfclist=[]
# 创建一个列表，用来储存客户点的食物。
k_dic={}
# 创建一个字典，用来储存客户点的食物的价格，方便结帐
k_dic={'主餐':0,'小食':0,'套餐':0,'饮料':0,'甜品':0}
 #<<<<<<<<<<这是菜单系统 项目的主要功能<<<<<<<<<<<<<<<<<<<<<<<<
def first():
    print('*'*50)
    print('欢迎来到kfc')
    print('1,光临人数') # 1-2=2人桌，3-4=4人桌，4位以上二楼上。
    print('2,美食主餐') # 就是汉堡肉卷啥的
    print('3,小食/薯条') # 薯条，爆米花
    print('4,欢乐套餐')
    print('5,缤纷饮料')
    print('6,冷饮甜品')
    print('7,结帐欢迎下次光临')
    print('8,退出系统')
    print('*'*50)
first()
# <<<<<<<<<<这是补充每个菜单的具体实现细节<<<<<<
def renshu() :
    user=int(input('你好，欢迎光临：请输入人数 '))
    # 从屏幕上获取 客户的人数
    if user==1:# and user==2:
        print('你好，请来两人桌')
    elif user==2:
        print('你好，请来两人桌')
    elif user==3:  # and user==4:
       print('你好，请来四人桌')
    elif user==4:
       print('你好，请来四人桌')
    else:
        print('你好，请来二楼有单间')
a=0 # 设置一个变量用来储存价格，用来结帐付款。
def zhushi(): # 定义一个函数，
    print('*'*50)
    print('1.虾堡15元,2.鸡堡12元,3.肉卷10元,4.退货,8.退出当前系统')
    print('*'*50)
    while True:
        global a
        b=15 # 把价格赋值给左边的变量，
        c=12
        d=10
        qq=input('你好，请问点些什么')
        if qq=='1':# 如果客户输入
            kfclist.append('虾堡')
            a=b+a
            print('您点的是: %s 价格：%d' % (kfclist,a))
        elif qq=='2':
            kfclist.append('鸡堡')
            a=c+a
            print('您点的是: %s 价格: %d' % (kfclist,a))
        elif qq=='3':
            kfclist.append('肉卷')
            a=d+a
            print('您点的是: %s 价格: %d' % (kfclist,a))
        elif qq=='4':
            ww=int(input('不好意思点多了麻烦退一下:'))
            if kfclist[ww-1]=='虾堡':
            # 下面使用的是del删除需要索引来删除;所以-1.
                a=a-15
            elif kfclist[ww-1]=='鸡堡':
                a=a-12
            elif kfclist[ww-1]=='肉卷':
                a=a-10
            del kfclist[ww-1]
            print(kfclist)
        elif qq=='8':
            print('您好，您此处消费 %d' % a)
            break
    k_dic['主餐']=a
    # 前面字典中定义的'主餐'的值是0,现在使用这个把里面的0替换掉。
z=0
def xiaoshi():
    global z
    while True:
        print('*'*50)
        print('1.薯条6元,2.爆米花18元,3.退货,8.退出当前系统')
        print('*'*50)
        st=6
        bm=18
        ww=int(input('您好，请问需要点些什么:'))
        if ww==1:
            kfclist.append('薯条')
            z=z+st
            print('您好，你点了: %s 价格: %s' % (kfclist,st))
        elif ww==2:
            kfclist.append('爆米花')
            z=z+bm
            print('您好，你点了: %s 价格: %s' % (kfclist,bm))
        elif ww==3:
            ee=int(input('不好意思，点错了，麻烦退一下:'))
            if kfclist[ee-1]=='薯条':
                z=z-6
            elif kfclist[ee-1]=='爆米花':
                z=z-18
            del kfclist[ee-1]
            print(kfclist)
        elif ww==8:
            print('您在此消费 %d元' % z)
            break
    k_dic['小食']=z
i=0
def taocan():
    while True:
        global i
        print('*'*50)
        print('1.吃过瘾炸鸡套餐58元，2.双拼鸡翅桶76元,3.葡式蛋挞6只36元 \n 4.退货，8.退出当前用户')
        print('*'*50)
        cc=58
        ss=76
        pp=36
        rr=int(input('您好,请问需要点些什么:'))
        if rr==1:
            kfclist.append('吃过瘾炸鸡套餐')
            i=i+cc
            print('您好，你点了: %s 价格: %d' % (kfclist,cc))
        elif rr==2:
            kfclist.append('双拼鸡翅桶')
            i=i+ss
            print('您好，你点了:',(kfclist,ss))
        elif rr==3:
            kfclist.append('葡式蛋挞6只')
            i=i+pp
            print('您好，你点了:',(kfclist,pp))
        elif rr==4:
            tt=int(input('不好意思，多点了麻烦退一下'))
            del kfclist[tt-1]
            print(kfclist)
        elif rr==8:
            print('您好，您在此消费 %d' %i)
            break
    k_dic['套餐']=i
l=0
def yinliao():
    while True:
        global l
        print('*'*50)
        print('1.可乐5元,2.咖啡15元，3.橙汁6元,4.退货，8.退出')
        print('*'*50)
        kk=5
        ff=15
        zz=6
        uu=int(input('您好，请问需要喝点什么?'))
        if uu==1:
            kfclist.append('可乐')
            l=l+kk
            print('您好，您点了: %s 价格: %d' % (kfclist,l))
        elif uu==2:
            kfclist.append('咖啡')
            l=l+ff
            print('您好，您点了: %s 价格: %d' % (kfclist,l))
        elif uu==3:
            kfclist.append('橙汁')
            l=l+zz
            print('您好，您点了: %s 价格: %d'% (kfclist,l))
        elif uu==4:
            ii=int(input('不好意思点错了帮我退一下:'))
            del kfclist[ii]
            print(kfclist)
        elif uu==8:
            print('您好，您在次系统一共消费 %d元' % l)
            break
    k_dic['饮料']=l
o=0
def tianpin():
    while True:
        global o
        print('*'*50)
        print('1.圣代12元，2.冰淇淋4元，3.奶茶8元，4.退货，8.退出')
        print('*'*50)
        m=12
        n=4
        v=8
        aa=int(input('您好请问需要来点什么:'))
        if aa==1:
            kfclist.append('圣代')
            o=o+m
            print('您好，您点了: %s 价格: %d' % (kfclist,m))
        elif aa==2:
            kfclist.append('冰淇淋')
            o=o+n
            print('您好，您点了: %s 价格: %d' % (kfclist,n))
        elif aa==3:
            kfclist.append('奶茶')
            o=o+v
            print('您好，您点了:',(kfclist,v))
        elif aa==4:
            ff=int(input('不好意思，帮我退一下:'))
            del kfclist[ff-1]
            print(kfclist)
        elif aa==8:
            print('您好，您在次共消费: %d元' % o)
            break
    k_dic['甜品']=o
# <<<<<<最后是结帐<<<<<<<<<<<<<<<<
def jiezhang():
    print('消费记录')
    print('主餐:',k_dic['主餐'])
    print('小食:',k_dic['小食'])
    print('套餐:',k_dic['套餐'])
    print('饮料:',k_dic['饮料'])
    print('甜品:',k_dic['甜品'])
    print('总消费:',k_dic['主餐']+k_dic['小食']+k_dic['套餐']+k_dic['饮料']+k_dic['甜品'])
    money=int(input('输入多少:'))
    money=money-k_dic['主餐']-k_dic['小食']-k_dic['套餐']-k_dic['饮料']- k_dic['甜品']

    print('您好给您找零 %d $' % money)
while True:
    user2=int(input('请输入功能'))
    if user2==1:
        renshu()
    elif user2==2:
        zhushi()
    elif user2==3:
        xiaoshi()
    elif user2==4:
        taocan()
    elif user2==5:
        yinliao()
    elif user2==6:
        tianpin()
    elif user2==7:
        jiezhang()
    elif user2==8:
        break









