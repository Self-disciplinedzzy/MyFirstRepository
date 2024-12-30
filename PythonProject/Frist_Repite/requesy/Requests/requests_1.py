import requests

q = input("请输入你想要知道的东西")
url = f'https://www.sogou.com/web?query={q}'

dic = {
    'Uset-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15'
}

resp = requests.get(url, headers=dic)   # 处理一个小小的反爬
print(resp)
print(resp.text)    # 拿到页面源代码

resp.close()
print("over")