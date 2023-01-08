# url = https://fanyi.baidu.com/sug

import requests

url = "https://fanyi.baidu.com/sug"

# s = input("你想翻译的英文:")
dic = {
    'Uset-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15'
}       #请求头
dat = {
    "kw": "dog"
}       #关键词

resp = requests.post(url, data=dat, headers=dic)
#print(resp.text)
print(resp.json())  # 将服务器返回的内容直接处理成json() => dic
resp.close()
print("over")
