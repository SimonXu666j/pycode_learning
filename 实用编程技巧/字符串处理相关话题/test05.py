#-*-coding:utf-8-*-
#如何将多个小字符串拼接成一个大的字符串？
#迭代列表，连续使用':'操作依次拼接每一个字符串
#使用str.join()方法，更加快速的拼接列表中所有字符串。
li=['simon','male','25']
# s=''
# for p in li:
#     s+=p
# print(s)
s=''.join(li)
print(s)
l=['abc',123,45,'xyz']
#列表解析
s1=''.join([str(x) for x in l])
print(s1)
#生成器表达式,减少开销
s2=''.join(str(x) for x in l)
print(s2)