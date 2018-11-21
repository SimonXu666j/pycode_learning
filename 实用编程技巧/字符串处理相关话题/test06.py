#-*-coding:utf-8-*-
#如何对字符串进行左、右、居中对齐？
#使用字符串的str.ljust(),str.rjust(),str.center()进行左，右，居中对齐
#使用format()方法，传递类似'<20','>20','^20'参数完成同样任务
s='abc'
print(s.ljust(20))
print(s.rjust(20))
print(s.center(20))
print(s.ljust(20,'='))

print(format(s,'<20'))
print(format(s,'>20'))
print(format(s,'^20'))

d={
    'Shanghai':25,
    'Beijing':24,
    'Hangzhou':23,
    'Suzhou':22
}
#找出最大长度
w=max(map(len,d.keys()))
#for k in d 和 for k in d.keys()等价
for k in d.keys():
    print(k.ljust(w),":",d[k])