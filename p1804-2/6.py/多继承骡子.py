class Lv(object):
    def manzou(self):
        print('走路慢')
    def jiao(self):
        print('驴子在汪汪汪汪')
class Ma(object):
    def shijian(self):
        print('持久')
    def jiao(self):
        print('小马在汪汪叫')
class Luozi(Lv,Ma):
    #def jiao(self):
     #   print('骡子在喵喵叫')
    pass
xiaoluo=Luozi()
xiaoluo.shijian()
xiaoluo.manzou()
xiaoluo.jiao()

