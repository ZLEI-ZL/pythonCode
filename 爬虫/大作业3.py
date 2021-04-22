import re
import requests
from urllib import error
import os

num = 0
numPicture = 0

#爬取并下载图片
def dowmloadPicture(html, keyword):
    global num

    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  #先利用正则表达式找到图片url

    print('找到关键词:' + keyword + '的图片，即将开始下载图片...')

    for each in pic_url:
        print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))

        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = file + r'\\' + keyword + '_' + str(num) + '.jpg' #存入信息
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()

            fo = open("图片地址", "a")
            fo.write(each+'\n')
            fo.close()

            num += 1
        if num >= numPicture:
            return


if __name__ == '__main__':  # 主函数入口
    word = input("请输入搜索关键词(可以是人名，地名等): ")

    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='

    numPicture = int(input("请输入要下载图片数量："))

    file = '图片文件'
    os.mkdir(file)

    t = 0

    tmp = url
    while t < numPicture:

        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)
            print(url)
        except error.HTTPError as e:
            print('网络错误，请调整网络后重试')
            t = t + 60
        else:
            dowmloadPicture(result.text, word)
            t = t + 60
