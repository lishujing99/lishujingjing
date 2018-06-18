class People:
    def __init__(self,name,yao,xiong,tun):
        self.name=name
        self.__yao=yao
        self.__xiong=xiong
        self.__tun=tun
    def ask_yao(self,sf):
        if sf=='医生':
            return self.__yao
        else:
            return 100
    def __sheng_wa(self):
        return '胖娃娃'
    def jie_hun(self,n):
        if n=='老王':
            print('不好意思')
        else:
            print('登记')
            print('旅游')
            print('%s给%s生了一个%s' % (self.name,n,self.__sheng_wa()))
huahu=People('花花',23,19,21)
#print(huahu.ask_yao('医生'))
print(huahu.jie_hun('老李'))


