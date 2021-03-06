#get the first page from maoyan

import requests
import re
import json, time
from config import *

#-------------------------------------------------------------------------------------------------
def get_1st_page(url):
    #set header
    #headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}


    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    return None
#-------------------------------------------------------------------------------------------------
def parse_1st_page(html):
    pattern= re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3])>3 else '',
            'time': item[4].strip()[5:] if len(item[4])>5 else '',
            'score': item[5].strip() + item[6].strip()
        }
    #print(items)

#-------------------------------------------------------------------------------------------------
def write_to_file(content):
    with open('result.txt','a', encoding='utf-8') as f:
        #print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
#-------------------------------------------------------------------------------------------------
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_1st_page(url)
    #print(html)
    #get movie content
    for item in parse_1st_page(html):
        print(item)
        write_to_file(item)
#-------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)