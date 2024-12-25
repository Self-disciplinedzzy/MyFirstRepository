"""
和爬虫v5一样，使用request.Request()，改进
"""
from urllib import parse
import json
import urllib.request

baseurl = 'http://fanyi.baidu.com/sug'

data = {
    'kw': 'girl'
}

data = parse.urlencode(data).encode('utf-8')

headers = {
    'Content-Length': len(data)
}
#原语法应该是rep = request.Request(url= baseurl, data= data, headers= headers)
#          rsp = request.urlopen(rep)
#但是调用request方法的时候必须要加urllib.这个前缀       就是说和网上老师教的语法结构不同
#我不知道我的代码和老师一样为什么就是结果不同，真是醉了
rep = urllib.request.Request(url= baseurl, data= data, headers= headers)
rsp = urllib.request.urlopen(rep)

json_data = rsp.read().decode('utf-8')
print(json_data)