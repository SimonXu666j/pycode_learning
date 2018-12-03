#-*-coding:utf-8-*-
from __future__ import print_function
import os

# print(os.path.realpath(__file__))    # 当前文件的路径
# print(os.path.dirname(os.path.realpath(__file__)))   # 从当前文件路径中获取目录
# print(os.path.basename(os.path.realpath(__file__)))  # 从当前文件路径中获取文件名
# print(os.listdir('.'))     # 只显示该目录下的文件名和目录名，不包含子目录中的文件，默认为当前文件所在目录


#递归获取指定文件夹下的所有文件名
li=[]
def f(d):
    for file in os.listdir(d): # os.listdir()得到当前路径下的文件和文件夹名字的列表  
        if os.path.isdir(file):
            f(file)
        else:
            # print(file,os.path.realpath(file))
            li.append(file)
    return li
        
print(f('.'))


# os.walk()遍历文件夹下的所有文件
# os.walk()获得三组数据(rootdir, dirname,filnames)
# def file_path(file_dir):
#     for root,dirs,files in os.walk(file_dir):
#         print(root,end=" ")   # 当前目录路径,end=""是python3的写法，python2中会报错，使用from __future__ import print_function兼容python2
#         print(dirs,end=" ")   # 当前路径下的所有子目录
#         print(files)          # 当前目录下的所有非目录子文件

# file_path('.')

# def f2(file_dir):
#     files_li=[]
#     for root,dirs,files in os.walk(file_dir):
#         for file in files:
#             files_li.append(file)
#     return files_li

# print(f2('.'))