while True:
    import random
    user=int(input('请玩家输入数字：'))
    dd=random.randint(1,10)
    print('电脑输出的数字是：%d' % dd)
    if user==6 and dd==5:
        print('用户胜出')
    elif user==dd:
        print('心有灵犀')
    else:
        print('电脑胜出')


