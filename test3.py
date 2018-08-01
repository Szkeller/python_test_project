# coding=utf-8
import requests
import re
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Host': 'movie.douban.com'
}
cookies = {'Cookie': '你自己的COOKIE'}
url = 'https://movie.douban.com/subject/26580232/comments?status=P'
html = requests.get(url, headers=headers, cookies=cookies)
reg = re.compile(r'<a href="(.*?)&amp;status=P".*?class="next">')
ren = re.compile(
    r'<span class="comment-info">.*? class="">(.*?)</a>.*?<span>.*?title="(.*?)"></span>.*?<span.*? title="(.*?)">.*?<p class="">(.*?)\n',
    re.S)
while html.status_code == 200:
    url_next = 'https://movie.douban.com/subject/26580232/comments' + re.findall(reg, html.text)[0]
    keren = re.findall(ren, html.text)
    data = pd.DataFrame(keren)
    print(data)
    print(url_next)
    data.to_csv('/Users/b1ancheng/Desktop/kerenduanping.csv', header=False, index=False, mode='a+',
                encoding="utf_8_sig")
    data = []
    keren = []
    html = requests.get(url_next, headers=headers, cookies=cookies)
    