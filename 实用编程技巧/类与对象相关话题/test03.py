#-*-coding:utf-8-*-
#如何让对象支持上下文管理？
'''
    解决方案：实现上下文管理协议，需定义实例的__enter__,__exit__方法，它们分别在with开始和结束时被调用。
'''
from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque

class TelnetClient(object):
    def __init__(self,addr,port=23):
        self.addr=addr
        self.port=port
        self.tn=None
    def start(self):
        self.tn=Telnet(self.addr,self.port) ##创建连接对象
        self.history=deque() ##创建队列，存储用户操作历史记录
        ##登陆操作
        t=self.tn.read_until('login:')
        stdout.write(t)
        user=stdin.readline()
        self.tn.write(user)

        t=self.tn.read_until('Password:')
        if t.startswith(user[:-1]):t=t[len(user)+1:]
        stdout.write(t)
        self.tn.write(stdin.readline())
        ##与服务器进行交互
        t=self.tn.read_until('$')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t=self.tn.read_until('$ ')
            stdout.write(t[len(uinput)+1:])
    def cleanup(self):
        self.tn.close()
        self.tn = None
        with open(self.addr+'_history.txt','w') as f:
            f.writelines(self.history)

##  如果使用上下文管理。。。
##  def __enter__(self):
##      self.tn=Telnet(self.addr,self.port) 
##      self.history=deque() ##将前面start函数中的两句命令移到这里来
##      return self
##  def __exit__(self,exc_type,exc_val,exc_tb):##后面三个是异常的类型，值，栈
##      self.tn.close()
##      self.tn = None
##      with open(self.addr+'_history.txt','w') as f:
##          f.writelines(self.history) ##将cleanup方法移到这里来
##  另外：当发生异常时则直接跳到__exit__方法，默认return None，程序不再允许
##  我们可以强调return True，则程序跳过异常继续执行

client=TelnetClient('127.0.0.1')
client.start()
client.cleanup()
'''
##上下文管理实现效果
with TelnetClient('127.0.0.1') as Client:
    client.start()  ##自动实现cleanup方法
'''