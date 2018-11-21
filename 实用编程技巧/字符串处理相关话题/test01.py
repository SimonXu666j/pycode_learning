#-*-coding:utf-8
#如何拆分含有多种分隔符的字符串？
'''
    方法一：连续使用str.split()方法，每次处理一种分隔符
    方法二：使用正则表达式的re.split()方法，一次性拆分字符串
'''
s='ab;s;3;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
# res=s.split(';')
# # print(res)
# t=[]
# map(lambda x:t.extend(x.split('|')),res)
# print(t)
# res=t
# t=[]
# map(lambda x:t.extend(x.split(',')),res)
# print(t)
# t=[]
# map(lambda x:t.extend(x.split('\t')),res)
# print(t)
def mySplit(s,ds):
    res=[s]
    for d in ds:
        t=[]
        map(lambda x:t.extend(x.split(d)),res)
        res=t
    return res
    #过滤空字符串
    # return [x for x in res if x]
r=mySplit(s,';,|\t')
print(r)