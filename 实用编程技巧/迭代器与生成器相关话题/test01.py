#-*-coding:utf-8-*-
# 如何实现可迭代对象和迭代器对象？
# 由可迭代对象得到迭代器
l=[1,2,3,4]
s="abcdefg"
# 迭代器对象<list_iterator object at 0x00000279FCADAA20>
t=iter(l)
print(t.next())
# print(t.__next__())  # python 3.x中 generator中的next变为__next__了。
