import csv
from lxml import etree
import requests
from multiprocessing.dummy import Pool
import time
headers = {
'Referer':'http://music.163.com/',
'Host':'music.163.com',
# 'User-Agent':'Mozilla/5.0 (X11: Linux *86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'User-Agent': 'Mozilla/5.0 (X11: Linux *86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',

    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
wangyi='http://music.163.com'
base_url='http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset={}'
urlList=[]      #保存构造出的链接
def totalPage():
    for i in range(0,1300,35):
        url=base_url.format(i)
        urlList.append(url)

def getData(url):
    r=requests.get(url,headers=headers)
    html=etree.HTML(r.text)
    MFlist=html.xpath("//p[@class='dec']/a/text()")
    MFurl=html.xpath("//p[@class='dec']/a/@href")
    LisNum=html.xpath("//span[@class='nb']/text()")
    for i in range(len(MFlist)):
        write.writerow([MFlist[i],wangyi+MFurl[i],LisNum[i]])
    time.sleep(3)   #延时，防止IP被封
f=open('Allmusicform.csv','a+',newline='',encoding='utf-8')
write=csv.writer(f)
p=Pool(4)
totalPage()
p.map(getData,urlList)
p.close()



