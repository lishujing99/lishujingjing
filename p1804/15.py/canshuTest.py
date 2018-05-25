
def a():
    print(12345)
def b():
    print(b)
a()

def canshu(q,w,e):
    print(q,w,e)
e=23
canshu(22,33,e)


def canshu1(*q):
    print(q)
haha=['lala','haha']
hihi=['hello',1,'hi']
canshu1(hihi,haha)



def add(a,b):
    print(a)
    print(b)
def addsan(a,b,c):
    a+b+c
def addsome(*sum):
    b=1
    for i in sum:
        b=b*i
    print(b)
addsome(1,2,3,4,5,6,)


