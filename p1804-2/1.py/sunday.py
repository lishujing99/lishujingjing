q=open('唐诗2.txt','w')
q.write('静夜思\n床前明月光\n疑是地上霜\n')
q.close()
q=open('唐诗2.txt','r')
w=q.readlines()
for i in w:
    print(i[0:-1] + '*')

q=open('唐诗2.txt','r')
e=q.readline()
r=q.tell()
print('当前读取的内容是: %s' % e)
print('当前游标位置是: %s' % r)

