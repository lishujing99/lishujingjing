while True:
    print('#'*18)
    import random
    dd=random.randint(1,3)
    user=int(input('用户输入的是'))
    print('电脑输出的是 %d :'% dd)
    if dd==1:
        print('电脑输出了小石头')
    elif dd==2:
        print('电脑输出了剪刀')
    else:
        print('电脑输出了布')
    if user==1:
        print('用户输出了小石头')
    elif user==2:
        print('用户输出了剪刀')
    else:
        print('用户输出了布')
    if user==1 and dd==2:
        print('user win')
    elif user==dd:
        print('ping')
    else:
        print('user lose')
    print('#'*18)
