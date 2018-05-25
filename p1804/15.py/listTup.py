dic={'name':'zhangsan','age':18,'sex':'nan','qq':123,'weixin':456}
# 创建一个字典
dic['name']# 根据key找出对应的value
print(dic['name']) # 在屏幕上显示出来
dic.get('name') # 同上
print(dic.get('name')) # 在屏幕上显示出来
klist=dic.keys()   #可以把全部的keys显示出来
print(dic.keys()) # 在屏幕上显示出全部的keys
print(klist)
vlist=dic.values()
print(dic.values())
print(vlist)
kvlist=dic.items()
print(kvlist)


dic={'name':'xiaoming','sex':'nv','age':16}
print(dic['name'])
print(dic['sex'])
k=dic.keys()
print(dic.keys())
v=dic.values()
print(dic.values())


for k,v in dic.items():
    print('k= ',k)
    print('v= ',v)


ilist=[{'北京':{'面积':'100平方','人口':'200w'}, '上海':{'面积':'80平方','人口':'150w'},'成都':{'面积':'75平方','人口':'130w'}}]

for i in ilist:
    for a,b in i.items():# a表示北京上海成都，b 表示{‘面积’，‘100平方’，‘人口’：‘100w’}
        for c,d in b.items():# c 表示 面积。d 表示人口
            print(a,c,d)

