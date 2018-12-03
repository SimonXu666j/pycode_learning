#-*-coding:utf-8-*-
#如何为创建大量实例节省内存？
'''
    解决方案：定义类的__slots__属性，它是用来声明实例属性名字的列表。
'''
#默认情况下Python用一个字典来保存一个对象的实例属性，对象多了就会很耗费内存。
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        

class MyClass1(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
