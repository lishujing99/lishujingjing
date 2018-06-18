class 人类(object):
    眼睛='黑色'
    __基因='x'  # 类属性
    def __init__(self):
        self.名字='张三'
        self.__性取向='正常'
p=人类()
print(p.名字)
print(人类.眼睛)
