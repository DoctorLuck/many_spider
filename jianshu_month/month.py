import requests
import re
from lxml import etree
from pymongo import MongoClient
import csv

class Spider:
    base_url='http://www.jianshu.com/trending/monthly?'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    param=[]
    article={}
    articleList=[]
    def getpage(self):
        for i in range(1,6):
            data='&'.join(self.param)
            url=self.base_url+data+'&page={}'.format(i)
            if i>=4:
                url=self.base_url+'utm_medium=index-banner-s&utm_source=desktop&'+data+'&page={}'.format(i)
            self.getID(url)
    def getID(self,url):
        f=open('Month.csv','a+',newline='',encoding='utf-8')
        write=csv.writer(f)
        client = MongoClient()      #用于写入MongoDB
        db = client.JianShuMonth    #用于写入MongoDB
        r=requests.get(url)
        print(r.url)
        html=etree.HTML(r.text)
        idList=html.xpath("//ul[@class='note-list']/li/@data-note-id")
        for id in idList:
            one='seen_snote_ids%5B%5D='+id
            self.param.append(one)
        name_list=html.xpath("//a[@class='blue-link']/text()")
        title_list=html.xpath("//a[@class='title']/text()")
        url_list=html.xpath("//a[@class='title']/@href")
        # print(name_list)
        for i in range(len(name_list)):
            self.article['author']=name_list[i]
            self.article['title']=title_list[i]
            self.article['url']='http://www.jianshu.com'+url_list[i]
            write.writerow([self.article['author'],self.article['title'],self.article['url']])
                # db.Monthly.insert_one({'author':self.article['author'],'title':self.article['title'],'url':self.article['url']})  用于写入MongoDB
s=Spider()
s.getpage()

