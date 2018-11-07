#-*-coding:utf-8-*-
# 如何实现可迭代对象和迭代器对象？
'''
    实现一个迭代器对象WeatherIterator,next方法每次返回一个城市气温。
    实现一个可迭代对象WeatherIterable,__iter__方法返回一个迭代器对象。
'''
from collections import Iterable,Iterator
import requests
# 查看抽象接口
# print(Iterable.__abstractmethods__)
# print(Iterator.__abstractmethods__)
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0
    def getWeather(self,city):
        r=requests.get("http://wthrcdn.etouch.cn/weather_mini?city="+city)
        data=r.json()['data']['forecast'][0]
        return '%s:%s  %s' % (city,data['low'],data['high'])
    # next()方法（Python 3.x 里是__next__()）会返回下一个迭代器对象。
    def next(self):
        if self.index==len(self.cities):
            raise StopIteration
        city=self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities=cities
    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable([u'北京',u'上海',u'广州',u'杭州']):
    print(x)