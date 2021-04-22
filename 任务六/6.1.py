import jieba

f = open("D:\\python代码\\任务五\\5.5.py", "rt", encoding = 'utf-8')

slist = []

for line in f:
    llist= jieba.lcut(line)
    
    for i in range(len(llist)):
        #if llist[i] not in {'import', 'try', 'in', 'input','for', 'if', 'range', 'except', 'break', 'else', 'int', 'print'}:
        llist[i] = llist[i].upper()

    slist.append(llist)
    
f.close

fo = open('D:\\python代码\\任务六\\6.1.1.py', "wt",encoding = 'utf-8')

for a in slist:
    fo.write(''.join(a))

fo.close()
