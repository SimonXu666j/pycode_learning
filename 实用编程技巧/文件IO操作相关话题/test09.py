#-*-coding:utf-8-*-
#如何读写json数据？
'''
    解决方案：
        使用标准库中的json模块，其中loads dumps函数可以完成json数据的读写。
        load dump的接口是文件
'''
import json
#dumps方法：将python对象转换成json字符串
l=[1,2,'abc',{'name':'simon','age':25}]
d={'b':None,'a':5,'c':'abc'}
l1=json.dumps(d,sort_keys=True)
l2=json.dumps(l,separators=[',',':'])
print(l1)
print(l2)
#loads方法：将json字符串转换成python对象
l11=json.loads(l1)
print(l11)
l21=json.loads(l2)
print(l21)

with open('demo.json','wb') as f:
    json.dump(l,f)

with open('demo.json','r') as fr:
    s=json.load(fr)
    print(s)