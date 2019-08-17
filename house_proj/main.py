#-*-coding:utf-8-*-

import requests
from lxml import html

init_url = 'https://sh.lianjia.com/ershoufang/xuhui/'

head = {'Host': 'sh.lianjia.com', 
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
}

if __name__ == '__main__':
    resp = requests.get(init_url, headers=head)
    tree = html.fromstring(resp.text)
    titles =  tree.xpath("//ul[@class='sellListContent']//div[@class='title']/a/text()")
    for t in titles:
        print t.encode('utf-8')