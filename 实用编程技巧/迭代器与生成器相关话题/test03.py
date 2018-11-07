#-*-coding:utf-8-*-
# 如何使用生成器函数实现可迭代对象？
def f():
    print("in f(),1")
    yield 1
    print("in f(),2")
    yield 2
    print("in f(),3")
    yield 3

g=f()
# print(g.next())
# print(g.next())
# print(g.next())
print(g.__iter__() is g)
for x in g:
    print(x)