import requests

url = "http://www.baidu.com/"
response = requests.get(url)
encoding='utf-8'
print(response.text)
