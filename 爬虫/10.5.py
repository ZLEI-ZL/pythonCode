# coding=utf-8
import requests
import re

# 存储爬取信息的列表
g_info = list()

# 58同城用奇异字符表示数字
g_dict = {'龒': '0', '驋': '1', '鸺': '2', '餼': '3', '龤': '4', '麣': '5', '閏': '6', '龥': '7', '鑶': '8', '齤': '9'}

#获取cookies信息
def get_session():

    s = requests.Session()

    s.headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://jj.58.com/chuzu/?PGTID=0d100000-008c-78a5-ac77-a44cc3330ee8&ClickID=2',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    s.get(url='https://jj.58.com/chuzu/')

    return s


def convert(s):
    """把&#x转换为ｕtf8最后转换为数字"""
    s = s.strip('&#x;')  # 例如把'&#x957f;'变成'957f'
    s = bytes(r'\u' + s, 'ascii')  # 把'xxxx'转换成b'\uxxxx'
    s = s.decode('unicode_escape')  # 把bytes转换为字符串,为奇异汉字
    s = g_dict.get(s, '')  # 将奇异汉字转换为数字
    return s


def get_content(html, info=g_info):
    # 诊断参数
    assert isinstance(html, str)
    if not info or not isinstance(info, list):
        info = g_info

    # 替换换行和&#x
    html = html.replace('\n', '')
    html = re.sub(r'&#x[a-f0-9]{4};', lambda match: convert(match.group()), html)

    # 获取li块列表
    ul = re.search(r'<ul class="house-list">(.*?)</ul>', html).group(1)

    lis = re.findall(r'<li .*? logr=".*?"\s+sortid=".*?">(.*?)</li>', ul)
    # 遍历li块列表,取具体的内容,存入列表
    for li in lis:

        temp = dict()
        temp['img'] = re.search(r'<.*?img-list.*?<a href="(.*?)" tongji_label="listclick', li).group(1)
        temp['name'] = re.search(r'<.*?strongbox.*?>(.*?)</a>', li).group(1)
        temp['name'] = re.sub(" ","",temp['name'])
        temp['money'] = re.search(r'<.*?money.*?<b class="strongbox">(.*?)</b>元/月\s*?</div>', li).group(1)
        ret = re.search(r'<.*?room">(.*?)\s+(&nbsp;)+(.*?)</p>', li)
        temp['house'] = ret.group(1) + ret.group(3)

        info.append(temp)

def save_content(info = g_info):
    if not info or not isinstance(info, list):
        info = g_info
    # 写入txt文件
    with open('58租房.txt', 'a', encoding='utf-8') as f:
        temp = "图片url：{}\n标题:{}\n\t价位:{:<8}户型:{}\n\n"
        for i in info:
             temp2 = temp.format(i["img"], i['name'], i['money'], i['house'])
             f.write(temp2)

#获取页面信息
def get_link(session, pindex=1):

    assert isinstance(session, requests.Session)

    url = 'https://bj.58.com/chuzu/'.format(int(pindex))

    res = session.get(url = url)

    get_content(res.text)

def main():
    try:
        pindex = int(input("请输入爬取的页码:"))
    except:
        pindex = 1

    s = get_session()

    get_link(session=s, pindex=pindex)

    save_content()


if __name__ == '__main__':
    main()
