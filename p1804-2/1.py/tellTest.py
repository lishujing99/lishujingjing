f=open('唐诗.txt','r')
f.readline()
y=f.tell()
print('读取的位置是 %d' % y)
f.readline()
u=f.tell()
print('读取的位置是 %d' % u)
f.readline()
i=f.tell()
print('读取的位置是 %d' % i)
f.readline()
o=f.tell()
print('读取的位置是 %d' % o)
f.readline()
p=f.tell()
print('读取的位置是 %d' % p)
f.close()

f=open('唐诗.txt','rb+')
q=f.readline()
w=f.seek(3,0)
print('内容是: %s' % q)
print('游标位置是: %d' % w)
# f=open('唐诗.txt','r')
e=f.readline()
r=f.seek(5,0)
print('内容是: %s' % e)
print('游标位置是: %d' % r)
t=f.readline()
y=f.seek(-3,1)
 # f=open('唐诗.txt','r')
u=f.readline()
i=f.seek(-8,2)
print('内容是: %s' % u)
print('游标位置是: %d' % i)

print('该文件的名字是: %s' % f.name)
print('该文件的打开模式是: %s' % f.mode)
print('该文件的关闭状态是: %s' % f.closed)




