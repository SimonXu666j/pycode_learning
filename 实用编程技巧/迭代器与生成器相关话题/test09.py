#-*-coding:utf-8-*-
#如何在一个for语句中迭代多个可迭代对象？
from random import randint
chinese=[randint(60,100) for _ in range(40)]
math=[randint(60,100) for _ in range(40)]
english=[randint(60,100) for _ in range(40)]
for i in range(len(math)):
    print(chinese[i],math[i],english[i])