# sample of JSON

import requests
import re

headers = {
    'User-Agent': 'Mozzila/5.0 (Michintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
try:
    r = requests.get("https://wwww.zhihu.com/explore", headers=headers)
   # pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    #titles = re.findall(pattern, r.text)
    print(r.text)
except requests.RequestException as err:
    print(err.strerror)