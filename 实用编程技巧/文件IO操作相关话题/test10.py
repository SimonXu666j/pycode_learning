#-*-coding:utf-8-*-
#如何解析简单的xml文档？
'''
    解决方法：
        使用标准库中的xml.etree.ElementTree，其中的parse函数可以解析xml文档。
'''
from xml.etree.ElementTree import parse
f=open('demo.xml')
et=parse(f)
root=et.getroot()
print(root,root.tag,root.attrib,root.text.strip())
# print(root.getchildren())
for child in root:
    print child.get('a_name')
print(root.find('class'))
print(root.findall('class'))
print(root.iterfind('class'))
for e in root.iterfind('class'):
    print e.get('a_name')
#返回所有元素节点
print(list(root.iter()))
print(root.findall('class/*'))
print(root.findall('.//student'))
print(root.findall('.//student/..'))
print(root.findall('class[@name]'))
print(root.findall('class[@a_name="1606D"]'))
print(root.findall('class[student]'))
print(root.findall('class[student="simon"]'))
print(root.findall('class[1]'))
print(root.findall('class[last()]'))