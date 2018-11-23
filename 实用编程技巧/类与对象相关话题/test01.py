#-*-coding:utf-8-*-
#如何派生内置不可变类型并修改实例化行为？
'''
    解决方案：定义类Intuple继承内置tuple，并实现__new__，修改实例化行为。
'''
class IntTuple(tuple):
    def __new__(cls,iterable):
        #创建生成器
        g=(x for x in iterable if isinstance(x,int) and x>0)
        #返回一个实例化对象，传入构造器方法
        return super(IntTuple,cls).__new__(cls,g)
        
    def __init__(self,iterable):
        #before
        print(self)
        super(IntTuple,self).__init__(iterable)
        #after



t=IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)