#-*-coding:utf-8-*-
#如何去掉字符串中不需要的字符
'''
1.字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符
2.删除单个固定位置的字符，可以使用切片+拼接的方式
3.字符串的replace()方法或正则表达式re.sub()删除任意位置字符
4.字符串translate()方法，可以同时删除多种不同字符
'''
import re
# s='abc:123'
# s1=s[:3]+s[4:]
# print(s1)
s='\tabc\t123\txyz\ropq\r'
# s1=s.replace('\t','')
# print(s1)
s2=re.sub('[\t\r]','',s)
print(s2)

#string的translate
s='abcerxyzw13r4'
import string
#映射表
string.maketrans('abcxyz','xyzzbc')
s1=s.translate(string.maketrans('abcxyz','xyzabc'))
print(s1)

s='abc\refg\n234\t'
#第一参数传None，去除匹配到的字符
s2=s.translate(None,'\t\r\n')
print(s2)

