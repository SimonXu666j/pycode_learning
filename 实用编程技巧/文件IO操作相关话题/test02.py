#-*-coding:utf-8-*-
#如何读写文本文件？
'''
python2.x-->python3.x字符串的语义发生了变化：
 str   ->     bytes
 unicode  ->  str
python2.x中：写入文件前对unicode编码，读入文件后对二进制字符串编码
python3.x中，open函数指定't'的文本模式，encoding指定编码格式。
'''
print("****python3.x中******")
# f=open('py3.txt','wt',encoding='utf-8')
# f.write('你好，我爱编程')
# f.close()

f=open('py3.txt','rt',encoding='utf-8')
s=f.read()
print(s)