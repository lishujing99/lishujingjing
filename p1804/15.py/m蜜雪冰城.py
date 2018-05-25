# 奶茶：主推口味：抹茶，香草i，草莓，哈密瓜;其他口味从屏幕上获取。
import random
import random
while True:
    a=random.randint(1,80)
    b=random.randint(1,80)
  #  time.sleep(0.5)
    print(a* ' ' , '蜜')
    print(a* ' ' , '雪')
    print(a* ' ' , '冰')
    print(a* ' ' , '城')
    print(b* ' ' , ' ❅ ')
    if a==10:
        break
    elif b==10:
        break
chadic={'奶茶选口味':0,'自主选口味':0}
naicha=[]
def caidan():
    print('*'*50)
    print('欢迎光临蜜雪冰城*6*')
    print('1,奶茶口味')
    print('2,自主选口味')
    print('3,结帐')
    print('4,会员卡')
    print('8,退出，退出，后会有其！')
    print('*'*50)
caidan()
z=0
def kouwei():
    global z
    a=15
    b=13
    c=16
    while True:
        print('<'*50)
        print('本店绝佳:*抹茶15*，*香草13*，*草莓16*')
        print('<'*50)
        user=input('请输入您需要的口味: ')
        if user=='抹茶':
            print('请稍等，马上给您做好;')
            naicha.append('抹茶')
            z=a+z
            print('您选的口味是  ;价格是: %d' % z)
        elif user=='香草':
            print('请稍等，马上给您做好;')
            naicha.append('香草')
            z=b+z
            print('您选的口味是  ;价格是: %d' % z)
        elif user=='草莓':
            print('请稍等，马上给您做好;')
            naicha.append('草莓')
            z=z+c
            print('您好，你点的是    价格是: %d' % z)
        elif user=='8':
            print('您好，您在此消费清单为: %s' % (naicha))
            print('您好，您在次 消费%d 元' % z)
            chadic['奶茶选口味']=z
            break
def zidian():
    while True:
        qq=input('^6^您好，前面没有喜欢的口味，欢迎来自主选口味^6^::')
        if qq!='8':
            print('喜欢这种口味呀^6^!')
            ww=int(input('请输入价格:'))
            print('您好您自选的口味是: %s 价格是: %s' % (qq,ww))
            chadic['自主选口味']=ww
        elif qq=='8':
            break
def jiezhang():
    print('啦啦啦…… 这么快就来结帐啦')
    print('奶茶口味:',chadic['奶茶选口味'])
    print('奶茶选口味:',chadic['自主选口味'])
     #money=chadic['奶茶选口味']+chadic['自主选口味']
    print('您好，您消费:' , chadic['奶茶选口味']+chadic['自主选口味'])

dic2={'会员名称':'无','会员卡号':'无','卡号密码':'无'}
money=0
ling1=0
def huiyuan():
    while True:
        print('1,创建会员')
        print('2,使用会员来结帐')
        print('8,后会有棋！')
        gg=int(input('小可爱你好，请问你要在在下这里使用什么功能?'))
        if gg==1:
            rr=input('创建会员名称:')
            tt=input('会员卡号:')
            yy=input('设置密码')
            uu=input('确认会员卡号:')
            ii=input('确认密码')
            if tt==uu and yy==ii:
                print('创建成功')
                aa=print('您已注册成功，欢迎加入我们的大家庭')
                print('首充100元会员享8折优惠')
                while True:
                    oo=int(input('请输入需要充值的金额: 8是退出充值哦！' ))
                    if oo==100:
                        print('充值成功！')
                        dic2['会员名称']=rr
                        dic2['会员卡号']=tt
                        dic2['卡号密码']=yy
                        print(dic2)
                        hh=print('您当前的余额为; %d' % oo)
                    elif oo==8:
                        break
            else:
                print('输入有误，需要重新输入哦')
        elif gg==8:
            break
        elif gg==2:
            print('您好。请输入卡号，密码方可打折')
            ff=input('名称')
            ss=input('账户')
            dd=input('密码')
            global rr
            if ff==rr:
                global money
                global ling1
                print('成功登录!')
                print('尊敬的vip小可爱;我们又见面了.')
                money=(chadic['奶茶选口味']+chadic['自主选口味'])*0.8
                print('打完折后的价格为: %s' % money)
                ling1=100-money
                print('从您的会员卡中扣除 %s 元  剩余 %s 元' % (money,ling1))
            elif dd!=yy:
                print('输入有错误，需要重新动一下手指头哦！')

while True:
    user2=int(input('您好，您需要什么:'))
    if user2==1:
        kouwei()
    elif user2==2:
        zidian()
    elif user2==3:
        jiezhang()
    elif user2==4:
        huiyuan()
    elif user2==5:
        dazhe()
    elif user2==8:
        break
