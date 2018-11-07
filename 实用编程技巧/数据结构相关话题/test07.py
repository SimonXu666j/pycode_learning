#-*-coding:utf-8-*-
#如何根据字典中值的大小，对字典中的项排序。
"""
    解决方案：使用内置函数sorted
            1.利用zip将字典数据转化元组
            2.传递sorted函数的key参数
"""
from random import randint
d={x:randint(60,100) for x in 'xyzabc'}
print(d)
# print(sorted(d))
# print(d.keys())
# print(d.values())
# zip(d.values(),d.keys())
# 利用zip将字典数据转化元组
# print(zip(d.itervalues(),d.iterkeys()))
print(sorted(zip(d.itervalues(),d.iterkeys())))

# 传递sorted函数的key参数
# print(d.items())
print(sorted(d.items(),key=lambda x:x[1]))