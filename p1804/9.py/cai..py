while True:
    import random
    dd=random.randint(1,100)
    user=int(input('请玩家输入数字'))
    print('玩家输入的数字：%d' % dd)
    if user==58 and dd==55:
        print('玩家胜出')
    elif user==dd:
        print('心有灵犀')
    else:
        print('电脑胜出')

