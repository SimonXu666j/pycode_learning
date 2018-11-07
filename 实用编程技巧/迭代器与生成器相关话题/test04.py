#-*-coding:utf-8-*-
# 如何使用生成器函数实现可迭代对象？
# 将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
class PrimeNumber:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def isPrimeNum(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k%i==0:
                return False
        return True
#将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.isPrimeNum(k):
                yield k

count=0
for x in PrimeNumber(1,100):
    print(x)
    count+=1
print("************")    
print("一共%d个素数" % count)