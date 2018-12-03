#-*-coding:utf-8-*-
#如何通过实例方法名字的字符串调用方法？
'''
    解决方案：
        方法一：使用内置函数getter，通过名字在实例上获取方法对象，然后调用。
        方法二：使用标准库operator下的methodcaller函数调用。
'''
#定义一个统一的接口函数，通过反射：getattr进行接口调用
from math import pi
  
  
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
  
    def getArea(self):
        return round(pow(self.radius, 2) * pi, 2)
  
  
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    def get_area(self):
        return self.width * self.height
  
  
# 定义统一接口
def func_area(obj):
    # 获取接口的字符串
    for get_func in ['get_area', 'getArea']:
        # 通过反射进行取方法
        func = getattr(obj, get_func, None)
        if func:
            return func()
    
  
if __name__ == '__main__':
    c1 = Circle(5.0)
    r1 = Rectangle(4.0, 5.0)
    
    # 通过map高阶函数，返回一个可迭代对象
    erea = map(func_area, [c1, r1])
    print(list(erea))