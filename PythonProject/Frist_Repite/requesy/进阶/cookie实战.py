import requests

url = "https://www.17k.com"
resp = requests.get(url)
resp.encoding="utf-8"
print(resp.text)