import requests
import re
import base64

t58_dict = {'龒':'0','龤':'1','驋':'2','閏':'3','餼':'4','麣':'5','鑶':'6','龥':'7','齤':'8','鸺':'9'}

def convert(s):
    """把&#x转换为utf8最后转换为数字"""
    s = s.strip('&#x;')  # 例如把'&#x957f;'变成'957f'
    s = bytes(r'\u' + s, 'ascii')  # 把'xxxx'转换成b'\uxxxx'
    s = s.decode('unicode_escape')  # 把bytes转换为字符串,为奇异汉字
    s = t58_dict.get(s, '')  # 将奇异汉字转换为数字
    return s

def zufang(html):

    pic_url = re.findall(r'<img lazy_src.*? src="(.*?)" data-loaded="true" >', html, re.S)

    print(html)

if __name__ == '__main__':

    headers = {
        'Host': 'bj.58.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer: https':'//bj.58.com/chuzu/?PGTID=0d100000-0000-10fc-fb8c-1d08324e485e&ClickID=2',
        'Connection': 'keep-alive',
        'Cookie': 'f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; userid360_xml=1B78B60CCA47FDF8B47BBDFD00639969; time_create=1565265541855; 58home=bj; id58=e87rZl0kURUNfzuUAxaCAg==; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; commontopbar_ipcity=bj%7C%E5%8C%97%E4%BA%AC%7C0; city=bj; 58tj_uuid=e80d8459-0b66-4b92-9d4e-86619793929a; new_uv=3; als=0; xxzl_deviceid=AaI3xBngax4AUqXPxRzuoihru7CjQbK0p0OV6yTKXRKyZW1J%2BlEt13R8yl9qQidZ; f=n; new_session=0; utm_source=; spm=; init_refer=https%253A%252F%252Fbj.58.com%252Fchuzu%252F%253FPGTID%253D0d100000-0000-119a-66a0-5bfc65666da7%2526ClickID%253D4',
        'Upgrade-Insecure-Requests': 1,
        'TE': 'Trailers'
    }

    url = 'https://bj.58.com/chaoyang/chuzu/?PGTID=0d3090a7-0000-197e-0b2a-92c67d7f79f1&ClickID=2'

    r = requests.get(url, headers)
    allResult = zufang(r.text)

    #printresult(allResult)