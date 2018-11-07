from collections import namedtuple
Student=namedtuple('Student',['name','age','sex','email'])
# 关键字传参
s=Student(name='simon',age=25,sex='male',email='1187819864@qq.com')
# 位置传参
s1=Student('simon',25,'male','15858224755@163.com')
print(s.name,s.age,s.sex,s.email)
print(s1.name,s1.age,s1.sex,s1.email)