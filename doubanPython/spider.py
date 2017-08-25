#coding:utf-8
import requests
import re
from lxml import etree
import csv

data={
    'q':'python',
    'start':'40',
    'cat':'1001'}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',}

base_url='https://www.douban.com/j/search?q=python&start={}&cat=1001'

def totalPage():
    for i in range(0,1001,20):
        url=base_url.format(i)
        getInfo(url)
def getInfo(url):
    r=requests.get(url,headers=headers).json()
    s=r['items']


    for i in s:
        res=etree.HTML(i)
        book_name=res.xpath("//h3/a/text()")[0]
        book_url=res.xpath("//h3/a/@href")[0]
        book_rate=res.xpath("//span[@class='rating_nums']/text()")
        if len(book_rate)==0:book_rate='暂无评价'
        else:book_rate=book_rate[0]
        # print(book_name,book_url,book_rate)
        write.writerow([book_name,book_url,book_rate])
f=open('pythonBook.csv','a+',newline='',encoding='utf-8')

write=csv.writer(f)
totalPage()

