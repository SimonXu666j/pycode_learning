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
N=randint(40,100)
history=deque([],5)
def guess(k):
    if k==N:
        print("right")
        return True
    elif k<N:
        print("%s is less than N" % k)
    else:
        print("%s is greater than N" % k)

while True:
    line=input("Please input a number:")
    if line.isdigit():
        k=int(line)
        history.append(k)
        if guess(k):
            break
    elif line=="history" or line=="h?":
        print(list(history))
        