#如何进行反向迭代已经如何实现反向迭代？
#实现反向迭代协议的__reversed__方法，它返回一个反向迭代器
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)

for y in FloatRange(1.0, 4.0, 0.5):
    print(y)