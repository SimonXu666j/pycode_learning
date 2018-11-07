#1.如何在列表，字典，集合中根据条件筛选数据？
'''
常规方法：迭代（筛选后append到一个新的列表）
高级方法：
    filter函数 filter(lambda x:x>=0,data),返回一个filter对象
    列表解析 [x for x in data if x>=0],返回一个列表     效率更高
    字典解析 {k:v for k,v in d.iteritems() if v>90}
    集合解析 {x for x in s if x%3==0}
'''
from random import randint
from timeit import timeit
data=[randint(-10,10) for _ in range(10)]
print(data)
data_change_01=filter(lambda x:x>=0,data)
data_change_02=[x for x in data if x>=0]
print(data_change_01)
print(data_change_02)
for i in data_change_01:
    print(i)

s=set(data)
change_s= {x for x in s if x%3==0}
print(change_s)