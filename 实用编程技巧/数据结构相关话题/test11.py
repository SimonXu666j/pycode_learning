#-*-coding:utf-8-*-
# 如何实现用户的历史记录功能（最多n条）？
'''
    使用容量为n的队列存储历史记录
    使用标准库collections中的deque，它是一个双端循环队列
    程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入
'''
from random import randint
from collections import deque
import pickle
q=deque([],5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
# print(q)
# 程序退出前，可以使用pickle将队列对象存入文件
# pickle.dump(q,open('history','wb'))
# 再次运行程序时将其导入
q2=pickle.load(open('history','rb'))
print(q2)