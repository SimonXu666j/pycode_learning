from random import randint
d={x:randint(60,100) for x in range(20)}
print(d)
# 在Python2.x中，items( )用于 返回一个字典的拷贝列表，占额外的内存。
# iteritems() 用于返回本身字典列表操作后的迭代，不占用额外的内存。
# python3.x 里用items()替换iteritems() ，可以用于 for 来循环遍历。
change_d={k:v for k,v in d.items() if v>90}
change_dx=d.items()
print(type(change_dx))
print(change_d)