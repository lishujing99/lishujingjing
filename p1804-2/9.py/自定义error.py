
#class Myerror(Exception):
  #  def __init__(self,str_error):
 #       self.name=str_error
#def get_pwd():
   # pwd=input('请输入密码')

  #  if len(pwd)<6:
 #       raise Myerror('密码必须大于六位.')
#try:

#    get_pwd()
#except Exception as q:
#    print('遇到异常:详情: %s' % q)


class Myer(Exception):
    def __init__(self,str_error):
        self.name=str_error
#class Myerr(Exception):
def get_a():
        con=input('输入用户名:')
        pwd=int(input('输入密码'))
        if pwd!=123456 and con !='李':
            raise Myer('输入有错误!')
try:
    get_a()
except Exception as w:
    print('遇到异常;详情:%s' % w)


