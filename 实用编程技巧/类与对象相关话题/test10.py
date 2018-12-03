#-*coding:utf-8-*-
#通过标准库operator中methodcaller方法进行调用
from math import pi
from operator import methodcaller
  
  
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
  
if __name__ == '__main__':
	  c1 = Circle(5.0)
	  r1 = Rectangle(4.0, 5.0)
    
    
	  # 第一个参数是函数字符串名字，后面是函数要求传入的参数，执行括号中传入对象
	  erea_c1 = methodcaller('getArea')(c1)
	  erea_r1 = methodcaller('get_area')(r1)
	  print(erea_c1, erea_r1)
    