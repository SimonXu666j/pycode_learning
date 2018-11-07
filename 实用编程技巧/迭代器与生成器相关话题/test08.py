#-*-coding:utf-8-*-
#如何对迭代器做切片操作？
#使用标准库中的itertools.islice,它能返回一个迭代对象切片的生成器。
from itertools import islice
f=open('messages')
#islice会消耗原来的迭代器对象，比如第一次迭代前面100到300个，那么迭代器里面剩下的从第301个开始，前面的都没了
# for line in islice(f,100,300):
#     print(line) 

f1=open("msg")
for line in islice(f1,3,6):
    print(line)

for line in islice(f1,1,3):
    print(line)