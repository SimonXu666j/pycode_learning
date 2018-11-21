#-*-coding:utf-8-*-
#如何使用临时文件？
'''
    解决方案：使用标准库中tempfile下的TemporaryFile(临时文件不用命名，且关闭后会被自动删除),NamedTemporaryFile
'''
from tempfile import TemporaryFile,NamedTemporaryFile
f=TemporaryFile()
f.write('abcdef'*10000)
f.seek(0)
f.read(100)

ntf=NamedTemporaryFile(delete=False)
print(ntf.name)