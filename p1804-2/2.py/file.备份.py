'''
a=input('你要复制的源文件是: ')
f=open(a,'r')
b=f.read()
b=input('要备份的新文件是: ')
f1=open(b,'w')
f1.write(b)
f.close()
f1.close()
'''

def copy(a,b):
    f=open(a,'r')
    while True:
        c=f.read(10)
        q=a.rfind('.')# 找到文件中.的下标位置
        q1=a[:q]# 截取文件.之前的部分
        q2=a[q:]# 截取文件.之后的部分
        f=open(q1+'-副本'+q2+b,'w')
        f.write(c)
        if len(c)==0:
            break
n=input('输入备份的文件名称:')
m=input('输入新文件的名字:')
copy(n,m)







