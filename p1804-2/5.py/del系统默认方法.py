class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        pass
    def set_name(self):
        f=open('name1.txt','w')
        #f.write(self.name)
        f.write(self.age)
        f.close()
        f=open('name1.txt','r')
        q=f.read()
        if len(q)!= 0:
            #self.age=q
            #self.name=q
            pass
        else:
            print('输入名字')
    def __del__(self):
        print('#2系统默认删除当前没有用的对象.')
huahua=People('花花','18')
huahua1=huahua
print('#1没有彻底删除对象，系统会不会先调用__del__ 默认删除')
print('#1必须彻底删除才能先调用__del__默认删除')
huahua.set_name()



