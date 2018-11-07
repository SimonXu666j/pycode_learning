#-*-coding:utf-8-*-
import re
from collections import Counter
txt=open('test.txt').read()
c=Counter(re.split(r'\W+',txt))   
print(c)
print(c.most_common(3))