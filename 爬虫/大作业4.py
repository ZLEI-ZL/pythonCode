import requests
import os
import re

allResult = []

def downloadtop10(html):

    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'+ '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    result = re.findall(pattern, html)

    allResult.append(result)

'''def downloadpicture(html):

    fail = '猫眼电影top10'
    os.mkdir(fail)'''

def printallResult(allResult):

    file = '猫眼电影top10'
    os.mkdir(file)

    fo = open("猫眼top10.txt", "w")
    for i in allResult:
        if i != None:
            for j in i:

                fo.write(str(j))

                print(j)

                url = str(j[1])
                name = str(j[2])

                pic = requests.get(url, timeout=7)
                string = file + r'\\' + name + '.jpg'
                fp = open(string, 'wb')
                fp.write(pic.content)
                fp.close()
    fo.close()


if __name__ == '__main__':

    t = 0
    while True:

        url = 'https://maoyan.com/board/4?offset=' + str(t)

        try:
            top10 = requests.get(url, timeout = 15)

            top10.encoding = 'utf-8'

            html = top10.text
        except:
            print("页面获取失败")

        allResult.append(downloadtop10(html))
        t += 10

        if t > 90:
            break
    printallResult(allResult)

