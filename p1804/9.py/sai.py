import random
a=random.randint(1,6)
b=random.randint(1,6)
c=random.randint(1,6)
d=a+b+c
print('请输入大小 %d, 请输入大小 %d ,请输入大小 %d , 请输入大小 %d' % (a,b,c,d))
if d>9:
    print('大大大')
else:
    print('小小小')



