import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLtext(url, code="uft-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        print("test")
        return r.text
    except:
        return ""

def getStocklist(list,stockURL):
    html = getHTMLtext(stockURL,"GB2312")
    print("getstockList start")
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            list.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(list,stockURL,filePath):
    print(stockURL)

    count = 0
    for stock in list:
        url = stockURL + stock + ".html"
        html = getHTMLtext(url)

        try:
            if html =="":
                continue

            infoDict = {}
            soup = BeautifulSoup(html,"html.parser")
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'}) [0]
            infoDict.update({'stock name': name.next.split()[0]})
            keylist=stockInfo.find_all('dt')
            valuelist = stockInfo.find_all('dd')

            for i in range(len(keylist)):
                key = keylist[i].text
                value = valuelist[i].text
                infoDick[key] = value

                with open(filePath,'a',encoding='utf-8') as f:
                    f.write(str(infoDict) + '\n')
                    count = count + 1
                    print("\r current processing: {:.2f}%",format(count*100/len(list,end="")))
        except:

            count = count + 1
            print("error")
            continue


def main():

    print("start")

    list_url = 'http://quote.eastmoney.com/stocklist.html'
    info_url = 'https://gupiao.baidu.com/stock/'
    output_file = '/Users/zhangkeller/BaiduStockInfo.txt'
    slist = []
    getStocklist(slist, list_url)
    getStockInfo(slist, info_url, output_file)
    print("end")

main()
