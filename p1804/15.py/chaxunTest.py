mingpian=[]
dic1={'name':'李舒静','com':'冰淇淋','qq':'12345'}
dic2={'name':'小鑫','com':'欣欣向荣公司','qq':'45678'}
dic3={'name':'张婷','com':'张二婷大酒店','qq':'22222'}
mingpian.append(dic1)
mingpian.append(dic2)
mingpian.append(dic3)
while True:
    chaxun=input('请输入要查询的名字:')
    for i in mingpian:
        if chaxun==i['name']:
            print('*'*30)
            print('姓名: %s' % i['name'])
            print('公司: %s' % i['com'])
            print('QQ: %s' % i['qq'])
            print('*'*30)
    if chaxun=='q':
            break
