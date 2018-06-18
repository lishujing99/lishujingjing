class People(object):
    guoji='中国' #类属性
    def __init__(self):
        self.name='小明' #实例属性
    def get_name(self): #实例方法
        return self.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji

print(People.guoji)
print(People.get_guoji())



