#-*-coding:utf-8-*-
#如何让类支持比较操作？
'''
    解决方案：比较运算符重载，需要实现__lt__ __le__ __gt__ __ge__ __eq__ __ne__
            使用标准库下的functools下的类装饰器total_ordering可以简化此过程。
'''
# class Rectangle(object):
#     def __init__(self,w,h):
#         self.w = w
#         self.h = h

#     def area(self):
#         return self.w * self.h


#     def __lt__(self,rect):
#         if self.area() < rect.area():
#             return True
#         else:
#             return False

#     def __le__(self,rect):
#         if self.area() <= rect.area():
#             return True
#         else:
#             return False

#     def __gt__(self,rect):
#         if self.area() > rect.area():
#             return True
#         else:
#             return False

#     def __eq__(self,rect):
#         if self.area() == rect.area():
#             return True
#         else:
#             return False
#     def __ne__(self,rect):
#         if self.area() != rect.area():
#             return True
#         else:
#             return False


# rect1 = Rectangle(1.0,2.0)
# rect2 = Rectangle(1.0,1.0)
# print rect1 < rect2

from functools import total_ordering
@total_ordering
class Rectangle2(object):
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self,rect):
        return self.area() < rect.area()

    def __eq__(self,rect):
        return self.area() == rect.area()


rect1 = Rectangle2(1.0,2.0)
rect2 = Rectangle2(1.0,1.0)
print rect1 >= rect2
