#-*-coding:utf-8-*-
#如何读写文本文件？
'''
python2.x-->python3.x字符串的语义发生了变化：
 str   ->     bytes
 unicode  ->  str
python2.x中：写入文件前对unicode编码，读入文件后对二进制字符串编码
python3.x中，open函数指定't'的文本模式，encoding指定编码格式。
'''
print(u"****python2.x中******")
s=u'你好'
print(s)
#encode编码变成str
print(s.encode('utf-8'))
print(s.encode('gbk'))
#decode解码变成unicode
print(s.encode('utf-8').decode('utf-8'))


# f=open('py2.txt','w')
# s=u'你好'
# f.write(s.encode('gbk'))
# f.close()

# f=open('py2.txt','r')
# t=f.read()
# print(t)