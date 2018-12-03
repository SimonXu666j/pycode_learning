#-*-coding:utf-8-*-
#如何使用多线程？
'''
    解决方案：
        使用标准库threading.Thread创建线程，在每一个线程中下载并转换一只股票数据。
        Python多线程的缺陷：在Python中，有一个GIL，即全局解释锁，该锁的存在保证在同一个时间只能有一个线程执行任务，
        也就是多线程并不是真正的并发，只是交替得执行。假如有10个线程炮在10核CPU上，当前工作的也只能是一个CPU上的线程。
        Python多线程在IO密集型任务中还是很有用处的，而对于计算密集型任务，应该使用Python多进程。
'''
import csv
from xml.etree.ElementTree import Element,ElementTree
import requests 
from StringIO import StringIO
from xml.dom.minidom import parse
from xml.dom import minidom
from test.test_heapq import SideEffectLT
from pip._vendor.requests.utils import get_environ_proxies

def download(url):
    proxies = {"http": "http://xx.yy.zz.ww:8000"}
    response = requests.get(url,proxies=proxies)
    if response.ok:
        return StringIO(response.content)

def createXmlFromCsv(scsv,fxml):
    root=minidom.Document()
    dataElement=root.createElement("Data")

    reader=csv.reader(scsv)
    headers=reader.next()
    headers = map(lambda h: h.replace(' ',''),headers)
    for row in reader:
        rowElement=root.createElement("Row")
        for tag,text in zip(headers,row):
            item=root.createElement(tag)
            item.appendChild(root.createTextNode(text))
            rowElement.appendChild(item)
        dataElement.appendChild(rowElement)
    fxml.write(root.appendChild(dataElement).toprettyxml())                            
    #return root.appendChild(dataElement)


if __name__ == '__main__':
    url = "http://table.finance.yahoo.com/table.csv?s=000001.sz"
    rf = download(url)
    if rf:
        with open("000001.xml",'wb') as wf:
            createXmlFromCsv(rf,wf)



from threading import Thread
def handle(sid):
    print "Download...%d"% sid
    url="http://table.finance.yahoo.com/table.csv?s=%s.sz"
    url %=str(sid).rjust(6,'0')
    rf = download(url)
    if rf is None: return
    print 'Convert to XML ...(%d)' % sid
    fname = str(sid).rjust(6,'0') + '.xml'
    with open (fname,'wb') as wf:
        createXmlFromCsv(rf,wf)    


import time
def handle2(sid):
    print "Counting... %d"%sid
    for i in [x for x in range(sid)]:
        time.sleep(0.01)

    print "Counting done %d"%sid


t = Thread(target=handle2,args=(1,))
t.start()

class MyThread(Thread):
    def __init__(self,sid):
        super(MyThread,self).__init__()
        self.sid = sid
    def run(self):
        handle2(self.sid)

t=MyThread(2)
t.start()


threads = []
for i in xrange(1,11):
    t = MyThread(i)
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print "main thread..."