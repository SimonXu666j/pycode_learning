#-*-coding:utf-8-*-
#如何线程间通信？
'''
    解决方案：
        使用标准库中Queue.Queue，它是一个线程安全的队列，Download线程把下载数据放入队列，Convert线程从队列里提取数据。
'''
from xml.etree.ElementTree import Element,ElementTree
from xml.dom.minidom import parse
from xml.dom import minidom
from threading import Thread
from collections import deque
from Queue import  Queue
from StringIO import StringIO
import requests
import csv
q2 =deque()


i=0

def pretty(e,level=0):
    if len(e) >0:
        e.text='\n' + '\t'*(level+1)
        for child in e:
            pretty(child,level+1)
        child.tail=child.tail[:-1]
    e.tail='\n' + '\t'*level


class DownloadThread(Thread):
    def __init__(self,sid,queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"
        self.url %= str(sid).rjust(6,'0')
        self.queue = queue

    def download(self,url):
        proxies = {"http": "http://135.245.48.34:8000"}
        #response = requests.get(url,proxies=proxies)
        #response = requests.get(url)
        #if response.ok:
        #    return StringIO(response.content)
        f = open("pingan.csv")
        #reader = csv.reader(f)
        #return StringIO(reader)
        import time
        if self.sid == 1:
            time.sleep(10)

        return StringIO(f.read())


    def run(self):

        print "download ",self.sid,self.url
        data = self.download(self.url)


        self.queue.put((self.sid,data))

class ConvertThread(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue = queue

    def createXmlFromCsv(self,scsv,fxml):
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


    def csvToXml(self,scsv,fname):
        reader=csv.reader(scsv)
        headers=reader.next()
        root=Element('Data')
        for row in reader:
            eRow=Element('Row')
            root.append(eRow)
            for tag,text in zip(headers,row):
                e=Element(str(tag).replace(" ", "_"))
                e.text=text
                eRow.append(e)
        pretty(root)
        et = ElementTree(root)
        et.write(fname)

    def run(self):
        print "xxyy....in csv thread"
        while True:
            import time
            print "xxyyzz....in csv thread",time.localtime()
            sid, data = self.queue.get()
            print "after getting xxyyzz....in csv thread",time.localtime
            if sid == -1:
                break
            if data:
                print 'Convert to XML ...(%d)' % sid
                fname = str(sid).rjust(6,'0') + '.xml'
                with open (fname,'wb') as wf:
                    self.createXmlFromCsv(data,wf)
                    #self.csvToXml(data,wf)

q=Queue()
dThreads=[DownloadThread(i,q) for i in xrange(1,4)]
cThreads=ConvertThread(q)

for t in dThreads:
    t.start()

cThreads.start()    

for t in dThreads:
    t.join()


print "main thread"

q.put((-1,None))