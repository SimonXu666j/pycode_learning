# 如何为元组中的每个元素命名，提高程序可读性？
# 方案1：定义枚举
# 方案2：使用标准库中collections.namedtuple代替内置tuple

# NAME=0
# AGE=1
# SEX=2
# EMAIL=3
NAME,AGE,SEX,EMAIL=range(4)
student=('simon',25,'male','1187819864@qq.com')
print(student[NAME])
print(student[AGE])
print(student[SEX])
print(student[EMAIL])