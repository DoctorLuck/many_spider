#coding:utf-8
import requests
import re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
data={
    'source':'李彦宏是马云最大威胁嘛？',
    'param1':'0.4',
    'param2':1}
r=requests.post('http://www.pullword.com/process.php',data=data)
print(r.text)