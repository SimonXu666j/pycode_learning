#-*-coding:utf-8-*-
#如何构建xml文档？
'''
    解决方案：
        使用标准库中的xml.etree.ElementTree，构建ElementTree，使用write方法写入文件。
'''
import csv
from xml.etree.ElementTree import Element, ElementTree #由element构成elementtree
from e2 import pretty

def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()  #读取了第一行

        root = Element('Data')  #构建了根节点
        for row in reader:  #这里指针已经去到数据行了
            eRow = Element('Row')  #创建子节点
            root.append(eRow)   #将子节点插入根节点
            for tag, text in zip(headers, row):  #迭代字典，就是将csv首行和数据行打包成字典，然后循环赋值
                e = Element(tag)
                e.text = text
                eRow.append(e)  #将孙子节点插入到子节点

    pretty(root)
    return ElementTree(root)

et = csvToXml('pingan.csv')
et.write('pingan.xml')
