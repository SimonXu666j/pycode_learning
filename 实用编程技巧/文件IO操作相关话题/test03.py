#-*-coding:utf-8-*-
#如何处理二进制文件？
'''
    open函数想以二进制模式打开文件，指定mode参数为'b'
    二进制数据可以用readinto，读入到提前分配好的buffer中，便于数据处理
    解析二进制数据可以使用标准库中的struct模块的unpack方法
'''
import struct
import array
f=open('demo.wav','rb')
info=f.read(44)
#音频文件的声道数
struct.unpack('h',info[22:24])
f.seek(0,2)
f.tell()
n=(f.tell()-44)/2
buf=array.array('h',(0 for _ in range(n)))
f.seek(44)
f.readinto(buf)
for i in range(n):
    buf[i]/=8
f2=open('demo2.wav','wb')
f2.write(info)
buf.tofile(f2)
f2.close()
#python3.x中字节需要前缀b,python2.x中unicode需要前缀u
# print(struct.unpack('h',b'\x01\x02'))
# print(struct.unpack('h','\x01\x02'))