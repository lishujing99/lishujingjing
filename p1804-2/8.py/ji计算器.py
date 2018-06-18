try:
    def jia(a,b):
        return a+b
    def jian(a,b):
        return a-b
    def cheng(a,b):
        return a*b
    def chu(a,b):
        return a/b
    class Father(object):
        aa=None
        bb=True
        def __init__(self,name):
            self.name=name
            Father.bb=self.name
        def jisuan(self,a):
            while True:
                fuhao=input('请输入符号:')
                if fuhao=='=':
                    break
                b=int(input('输入数字:'))
                if fuhao=='+':
                    a=jia(a,b)
                elif fuhao=='-':
                    a=jian(a,b)
                elif fuhao=='*':
                    a=cheng(a,b)
                elif fuhao=='/':
                    a=chu(a,b)
                #elif fuhao=='q':
                 #   break
            print('运算结果为: %d' % a)


        def __new__(cls,*k):
            if cls.aa==None:
                cls.aa=super().__new__(cls)
            return cls.aa
    jisuanji=Father('计算机')
    c=int(input('输入数字:'))
    #Father.jisuan(c)
    jisuanji.jisuan(c)
except Exception as r:
    print('程序报错: %s' % r)
