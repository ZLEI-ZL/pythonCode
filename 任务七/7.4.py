import jieba

def get_text():
    f = open('D:\\python代码\\任务七\\三国演义075回.txt','r').read()
    words = jieba.lcut(f)
    return words


words = get_text()

counts = {}
includes = ['直至','不如','荆州','一面','公安','众将','大喜','将军','左右','城门',
            '却说','商议','江东',]


for i in words:
    if len(i)==1 or i in includes:
        continue
    elif i in ['丞相']:
        counts['曹操'] = counts.get('曹操', 0) + 1
    elif i in ['孔明曰']:
        counts['孔明'] = counts.get('孔明', 0) + 1
    elif i in ['玄德曰','玄德']:
        counts['刘备'] = counts.get('刘备', 0) + 1
    elif i in ['关公','云长']:
        counts['关羽'] = counts.get('关羽', 0) + 1
    elif i in ['都督']:
        counts['周瑜'] = counts.get('周瑜', 0) + 1
    else:
        counts[i] = counts.get(i,0)+1

ls = list(counts.items())
ls.sort(key= lambda x:x[1],reverse=True)

for i in ls[:20]:
    print(i)
