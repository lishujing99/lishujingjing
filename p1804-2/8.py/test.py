class Cat(object):
    __instance=None
    def __new__(cls,name):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
        return cls.__instance
xiao=Cat('小')
da=Cat('da')
print(id(xiao))
print(id(da))








