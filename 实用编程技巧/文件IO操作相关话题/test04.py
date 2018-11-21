#-*-coding:utf-8-*-
#如何设置文件的缓冲？
'''文件的缓冲行为：全缓冲、行缓冲、无缓冲
    块缓冲区，一块4096个字节
    解决方案：
        全缓冲：open函数的buffering设置为大于1的整数n，n为缓冲区大小
        行缓冲：open函数的buffering设置为1
        无缓冲：oepn函数的buffering设置为0
'''
f=open('demo1.txt','w', buffering=2048)
f=open('demo2.txt','w', buffering=1)
f=open('demo3.txt','w', buffering=0)