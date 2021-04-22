import requests
import json
import hashlib
import time
import random

def main():

    keyWord = getKeyword()
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    result = processK(url, keyWord)

    printResults(result)

# 获取单词
def getKeyword():

    k =  input('请输入要翻译的英文：')

    return k

#爬取有道
def processK(url, k):

    try:

        #破解反爬
        client = 'fanyideskweb'
        ctime = int(time.time() * 1000)
        salt = str(ctime + random.randint(1, 10))
        key = '97_3(jkMYg@T[KZQmqjTK'
        sign = hashlib.md5((client + k + salt + key).encode('utf-8')).hexdigest()

        #定义字典和头部请求
        data = {}
        data['i'] = k
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = salt
        data['sign'] = sign
        data['ts'] = ctime
        data['bv'] = 'e2a78ed30c66e16a857c5b6486'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CL1CKBUTTON'

        head = {}
        head['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        head['Accept-Encoding'] = 'gzip, deflate'
        head['Accept-Language'] = 'zh-CN,zh;q=0.9'
        head['Connection'] = 'keep-alive'
        head['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        head[
            'Cookie'] = 'OUTFOX_SEARCH_USER_ID=-1645744815@10.169.0.84; JSESSIONID=aaa9_E-sQ3CQWaPTofjew; OUTFOX_SEARCH_USER_ID_NCOO=2007801178.0378454; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=' + str(ctime)
        head['Host'] = 'fanyi.youdao.com'
        head['Origin'] = 'http://fanyi.youdao.com'
        head['Referer'] = 'http://fanyi.youdao.com/'
        head[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        head['X-Requested-With'] = 'XMLHttpRequest'

        #爬取
        r = requests.post(url, data = data, headers = head)

        html = r.text

        ret_dict = json.loads(html)

        return ret_dict

    except:

        print('出错了！')

#打印结果
def printResults(result):

    print("------------->翻译内容<-------------")
    print(result['translateResult'][0][0]['src'])
    print("------------->翻译结果<-------------")
    print(result['translateResult'][0][0]['tgt'])
    print("------------->详细信息<-------------")

    l = result['smartResult']['entries']

    for i in range(len(l)):

        print(l[i])

main()