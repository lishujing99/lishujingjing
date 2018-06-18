class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def jump(self):
        print(' %s跳了一支舞' % self.name)
        print('等一场秋风再起，为你起舞')
    def singer(self):
        print(' %s唱了一首歌' % self.name)
        print('不如高歌一曲忘却烦恼')
    def qin(self):
        print(' %s谈了一首钢琴曲' % self.name)
        print('守望着天空，钢琴，和你的回忆')
    def di(self):
        print(' %s吹了一首笛子' % self.name)
        print('一篇诗，一斗酒，一曲长笛')
    def jian(self):
        print(' %s练了一会剑花' % self.name)
        print('愿你把酒执剑，归来仍是少年')
    def __str__(self):
        q='我的名字是:'+self.name + '我的年龄是:'+self.age
        return q
xiaowu=people('小舞','18') # 用来创建一个对象
print('我的介绍是:' , xiaowu)
xiaowu.jump()
 #xiaowu.name='小舞'
 #xiaowu.age='18'
xiaoge=people('小歌','19')
 #xiaoge.name='小歌'
 #xiaoge.age='19'
print('我的介绍是:' , xiaoge)
xiaoge.singer()
xiaoqin=people('小秦','16')
print('我的介绍是:' , xiaoqin)
xiaoqin.qin()
xiaodi=people('笛笛','17')
print('我的介绍是:' , xiaodi)
xiaodi.di()
xiaojian=people('小浅','15')
print('我的介绍是:' , xiaojian)
xiaojian.jian()

