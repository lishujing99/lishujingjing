class Worker:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def set_salary(self,new_salary):
        if new_salary>self.salary:
            self.salary=new_salary
        else:
            print('拒绝')
    def get_salary(self,shenfen):
        if shenfen=='媳妇':
            print( 1000 )
        elif shenfen=='朋友':
            print(100000)
        elif shenfen=='老爹':
            print(self.salary)
        else:
            print(0)
xyy=Worker('喜羊羊',10000)
#q=input('新工资:')
#print('工资现在是=%d' % xyy.salary)
while True:
    shenf=input('想知道我的工资吗？请说明你的身份:')
    xyy.get_salary(shenf)
    if shenf=='q':
        print('无可奉告')
        break


