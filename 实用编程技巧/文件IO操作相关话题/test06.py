#-*-coding:utf-8-*-
#如何方法文件的状态？
'''
    解决方案：
        系统调用：标准库os模块下的三个系统调用stat fstat lstat 获取文件状态。
        快捷函数：标准库os.path下一些函数，使用起来更加简洁。
'''
# import stat
# import os
# import time
# s=os.stat('test.sh')
# print(s)
# print(stat.S_ISDIR(s.st_mode))
# print(stat.S_ISREG(s.st_mode))
# print(s.st_mode & stat.S_IRUSR)
# print(time.localtime(s.st_atime))


import os
print(os.path.isdir('py3.txt'))
print(os.path.islink('py3.txt'))
print(os.path.isfile('py3.txt'))
print(os.path.getatime('py3.txt'))
print(os.path.getctime('py3.txt'))
print(os.path.getmtime('py3.txt'))
print(os.path.getsize('py3.txt'))