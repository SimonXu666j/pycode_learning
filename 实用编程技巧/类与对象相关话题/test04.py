#-*-coding:utf-8-*
#如何创建可管理的对象属性？
'''
    解决方案：使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问。
'''
from math import pi
class Circle(object):
    def __init__(self,radius):
        self.radius = radius


    def getRadius(self):
        return self.radius


    def setRadius(self,value):
        if not isinstance(value,(int,long,float)):
            raise ValueError('wrong type.')
        self.radius = float(value)

    def getArea(self):
        return self.radius **2 *pi

    R = property(getRadius,setRadius)

c2=Circle(1.0)
c2.R=2.0
print c2.getArea()