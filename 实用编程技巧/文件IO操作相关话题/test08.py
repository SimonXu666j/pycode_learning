#-*-coding:utf-8-*-
#如何读写csv数据？
'''
    解决方案：
        使用标准库中的csv模块，可以使用其中reader和writer完成csv文件读写。
'''
from urllib import urlretrieve
urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz','pingan.csv')
import csv
rf=open('pingan.csv','rb')
reader=csv.reader(rf)
reader.next()
for row in rf:
    print row

wf=open('pingan_copy.csv','wb')
writer=csv.writer(wf)
writer.writerow(['abc',123])
wf.flush()