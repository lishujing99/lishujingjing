class lingshi(): # 创建一个零食的类
    def buy(self):
        print('%s去超市买零食' % self.name)
    def eat(self):
        print(' %s去吃零食' % self.name)
    def introduce(self):
        print('我的名字是%s,我的颜色是%s ' % (self.name,self.color,))
shupian=lingshi() # 用类创建一个对象1
shupian.weight='1000k' # 给薯片的属性，重量
shupian.color='blue'   # 薯片的属性，样式
shupian.name='shupian'
shupian.introduce()
shupian.buy()
shupian.eat()
baomihua=lingshi()
baomihua.weight='1200k'
baomihua.color='red'
baomihua.name='baomihua'
baomihua.introduce()
baomihua.buy()
baomihua.eat()



