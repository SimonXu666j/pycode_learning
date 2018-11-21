#-*-coding:utf-8-*-
#如何判断字符串a是否以字符串b开头？
#使用字符串的str.startswith()和str.endswith()方法，
#注意：多个匹配时参数使用元组
import os,stat
file_names=os.listdir('.')
#列表解析
res_li=[file for file in os.listdir('.') if file.endswith(('.py','.sh'))]
print(res_li)
print(oct(os.stat('test01.py').st_mode))
# 添加可执行权限
os.chmod('test01.py',os.stat('test01.py').st_mode | stat.S_IXUSR)
print(oct(os.stat('test01.py').st_mode))