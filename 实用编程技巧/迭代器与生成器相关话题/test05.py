#如何进行反向迭代已经如何实现反向迭代？
l=[1,2,3,4,5]
print(l)
# 改变原列表
l.reverse()
print(l)
# 生成新列表
print(l[::-1])
# 列表反向迭代器
print(reversed(l))
for x in reversed(l):
    print(x)
