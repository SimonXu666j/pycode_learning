#-*-coding:utf-8-*-
#如何将文件映射到内存？
'''
    解决方案：
        使用标准库中mmap模块的mmap()函数，它需要一个打开的文件描述符作为参数
'''
import mmap
f=open('demo.bin','r')
m=mmap.mmap(f.fileno(),mmap.PAGESIZE*8,access=mmap.ACCESS_WRITE,offset=mmap.PAGESIZE*4)