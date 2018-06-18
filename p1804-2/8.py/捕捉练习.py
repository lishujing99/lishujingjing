q=input('输入文件名称：')
try:
    f=open(q,'r')
    w=f.read()
    print(w)
except:
    print('错误')
