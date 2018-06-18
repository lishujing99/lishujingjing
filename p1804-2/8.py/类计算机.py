class Jisu(object):
    def jia(a,b):
        return a+b
    def jian(a,b):
        return a-b
    def cheng(a,b):
        return a*b
    def chu(a,b):
        return a/b
ee=int(input('请输入数字:'))
while True:
    qq=input('请输入符号:')
    if qq=='=':
        break
    w=int(input('请输入数字:'))
    if qq=='+':
        ee=jia(ee,w)
    elif qq=='-':
        ee=jian(ee,w)
    elif qq=='*':
        ee=cheng(ee,w)
    elif qq=='/':
        ee=chu(ee,w)
print('总结果为: %d' % ee)

