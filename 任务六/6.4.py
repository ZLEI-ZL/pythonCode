#e14.1csv2json.py

coding = 'utf-8'

import json

fr= open("D:\\python代码\\任务六\\price2016bj.csv", "r")

ls = []

for line in fr:

    line = line.replace("\n","")
    ls.append(line.split(','))

fr.close()

fw= open("D:\\python代码\\任务六\\price2016bj.json", "w")

for i in range(1,len(ls)):

    ls[i] = dict(zip(ls[0], ls[i]))

    json.dump(ls[1:],fw, sort_keys=True, indent=4)
    
fw.close()
