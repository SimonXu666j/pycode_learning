#-*-coding:utf-8-*-
def pretty(e,level=0):
    if len(e)>0:
        e.text='\n'+'\t'*(level+1)#先换行，然后给level个Tab
        for child in e:
            pretty(child,level+1)#递归给tab
        child.tail = child.tail[:-1]#tail不懂（尾部的意思），这是对倒数第二行(子节点结尾)进行操作
        #如果不操作，子节点结尾就会跟孙子节点一样缩进了
    e.tail = '\n' +'\t' *level#这是对最后一行进行操作