# 如何快速找到多个字典中的公共键(key)？
from random import randint,sample
li=sample('abcdedfg',randint(3,6))
# print(li)
s1={x:randint(1,4) for x in sample('abcdedfg',randint(3,6))}
s2={x:randint(1,4) for x in sample('abcdedfg',randint(3,6))}
s3={x:randint(1,4) for x in sample('abcdedfg',randint(3,6))}
# print(s1)
# print(s2)
# print(s3)
# 方法一：将同时存在的key保存到一个新的列表，用in判断
# res=[]
# for k in s1:
#     if k in s2 and k in s3:
#         res.append(k)
# print(res)