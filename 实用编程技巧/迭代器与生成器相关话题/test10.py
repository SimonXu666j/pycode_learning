#-*-coding:utf-8-*-
#如何在一个for语句中迭代多个可迭代对象？
# 并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
# 串行：使用标准库中的itertools.chain，它能将多个可迭代对象连接。
from random import randint
# print(zip([1,2,3,4],('a','b','c','d')))
chinese=[randint(60,100) for _ in range(40)]
math=[randint(60,100) for _ in range(40)]
english=[randint(60,100) for _ in range(40)]
total=[]
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
print(total)

print("******************")
from itertools import chain
# for x in chain([1,2,3,4],('a','b','c','d')):
#     print(x) 
score1=[randint(60,100) for _ in range(40)]
score2=[randint(60,100) for _ in range(42)]
score3=[randint(60,100) for _ in range(42)]
score4=[randint(60,100) for _ in range(39)]
count=0
for s in chain(score1,score2,score3,score4):
    if s>90:
        count+=1
print(count)