# 如何统计出序列中元素出现的频度？
# 解决方案：将序列传入Counter的构造器，得到Counter对象的元素频度的字典
#           Counter.most_common(n)方法得到频度最高的n个元素的列表
from random import randint
from collections import Counter
li = [randint(0,20) for _ in range(30)]
c=dict.fromkeys(li,0)
# print(c)
for x in li:
    c[x]+=1
print(c)
c2=Counter(li)
print(c2)
# 找出出现频数最高的三个元素
print(c2.most_common(3))