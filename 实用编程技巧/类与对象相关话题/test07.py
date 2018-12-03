#-*-coding:utf-8-*-
#如何使用描述符对实例属性做类型检查？
'''
    解决方案：使用描述符来实现需要类型检查的属性，分别实现__get__ __set__ __delete__方法，
            在__set__内使用isinstance函数做类型检查。
'''
class Attr(object):
    def __init__(self,name,type_):
        self.name = name
        self.type_ = type_
    def __get__(self,instance,cls):
        print 'in__get__',instance,cls
        return instance.__dict__[self.name]   

    def __set__(self,instance,value):
        print 'in __set__'
        if not isinstance(value,self.type_):
            raise TypeError("expected is %s"%(self.type_))
        instance.__dict__[self.name] = value

    def __delete__(self,instance):
        print 'in __del__'
        del instance.__dict__[self.name]

class Person(object):
    name = Attr('name',str)
    age = Attr('age',int)
    height = Attr('height',float)

p=Person()
p.name='bob'
p.name=12