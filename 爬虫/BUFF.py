import requests
import re
from bs4 import BeautifulSoup

class BUFF():
    def __init__(self):
        self.url = 'https://buff.163.com/market/?game=csgo#tab=selling&page_num=1&category_group=knife'

    def process(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            print(r.text)
        except:
            print("网页获取异常")



if __name__ == '__main__':
    buff = BUFF()

    buff.process()