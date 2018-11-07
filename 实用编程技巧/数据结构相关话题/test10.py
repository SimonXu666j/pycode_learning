#-*-coding:utf-8-*-
# 如何让字典保持有序？
'''
    使用collections.OrderedDict
    以OrderedDict替代内置字典Dict，依次将选手成绩存入OrderedDict
'''
from collections import OrderedDict
from time import time
from random import randint
# d=OrderedDict()
# d['simon']=(1,34)
# d['button']=(2,35)
# d['jim']=(3,37)
# for k in d:
#     print(k)
d=OrderedDict()
players=list('ABCDEFGH')
start=time()
for i in range(8):
    raw_input()
    p=players.pop(randint(0,7-i))
    end=time()
    print(i+1,p,end - start)
    d[p]=(i+1,end-start)

print(d)