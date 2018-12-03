#-*-coding:utf-8-*-
#如何在环状数据结构中管理内存？
'''
    解决方案：
            使用标准库weakref，它可以创建一种能访问对象但不增加引用计数的对象
'''
# import weakref
# import sys
# class A(object):
#     def __del__(self):
#         print 'in A.__del__'

# a=A()
# print sys.getrefcount(a)
# a2=a
# print sys.getrefcount(a)
# a_wref = weakref.ref(a)
# a4 = a_wref()
# print sys.getrefcount(a)
# del a2
# del a 
# print "end.."




import weakref
class Data(object):
    def __init__(self,value,owner):
        self.owner = weakref.ref(owner)
        self.value = value

    def __str__(self):
        return "%s's data value is %s"%(self.owner(),self.value)

    def __del__(self):
        print 'in Data.__del__'

class Node(object):
    def __init__(self,value):
        self.data = Data(value,self)
        print self.data

    def __del__(self):
        print 'in Node.__del__'

node = Node(100)
del node
raw_input("waiting...")