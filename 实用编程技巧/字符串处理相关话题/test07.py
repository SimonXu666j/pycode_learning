#-*-coding:utf-8-*-
#如何去掉字符串中不需要的字符
'''
1.字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符
2.删除单个固定位置的字符，可以使用切片+拼接的方式
3.字符串的replace()方法或正则表达式re.sub()删除任意位置字符
4.字符串translate()方法，可以同时删除多种不同字符
'''
s='  123  abc    '
s1=s.strip()
s2=s.lstrip()
s3=s.rstrip()
print(s1)
print(s2)
print(s3)