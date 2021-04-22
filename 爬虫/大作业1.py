import requests
import json

def main():

    url = 'https://fanyi.baidu.com/sug'

    k = getKeywords() #获取查询单词

    date = search(url, k) #或取百度词典页面信息，并查询返回结果

    printResults(date) #打印结果

def getKeywords():

    keyWord = input("请输入要翻译词：")

    return keyWord

def search(url, keyWord):

    try:

        dic = {'kw' : keyWord} #定义字典

        r = requests.post(url, data = dic)

        r.encoding = 'utf-8'

        str1 = r.text

        str_dic = json.loads(str1) #解码获得的网页信息

        str_dic = str_dic['data'][0]['v']

        return str_dic

    except:

        print('出错了！')

def printResults(date):

    print("翻译结果为：{}".format(date))

main()
