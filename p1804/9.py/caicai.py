while True:
    import random
    dd=random.randint(1,3)
    print('#'*20)
    user=int(input('请输入数字：'))
    if dd==1:
        print('dn出石头')
    elif dd==2:
        print('dn出剪刀')
    else:
        print('dn出布')
    if user==1:
        print('user出石头')
    elif user==2:
        print('user出剪刀')
    else:
        print('user出布')



    if user==1 and dd==2 or user==2 and dd==3 or user==3 and dd==1:
        print('user win')
    elif user==dd:
        print('pingle')
    else:
        print('user lose')
    print('#'*20)



