class Test(object):
    def __init__(self):
        self.switch=input('输入开关:')
    def div(self,a,b):
        try:
            return a/b
        except Exception as q:
            if self.switch=='open':
                print('出现异常:%s' % q)
            else:
                raise
t=Test()
print(t.div(2,0))

