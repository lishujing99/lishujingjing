import os
def menu():
    print('1,创建目录')
    print('2,删除目录')
    print('3,查看目录')
    print('4,改变目录')
menu()


def cjml(a):
    os.mkdir(a)
def scml(b):
    os.rmdir(b)
def ckml():
    return os.getcwd()
def gbml(c):
    os.chdir(c)
list1=[]
while True:
    user=input('请输入功能: ')
    if user=='1':
        b=input('创建的目录名称是: ')
        cjml(b)
        list1.append(b)
    elif user=='2':
        q=input('删除的是: ')
        scml(q)
    elif user=='3':
        print(ckml())
    elif user=='4':
        e=input('输入改变的: ')
        gbml(e)
    elif user=='8':
        break






