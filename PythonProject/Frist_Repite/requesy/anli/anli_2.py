import requests
import csv
from bs4 import BeautifulSoup
import time

url = "http://m.netbian.com/s/chaogaoqing/"
resp = requests.get(url)
resp.encoding = "gbk"   #解码
resp_text = resp.text
#实例解析
bs = BeautifulSoup(resp_text, "html.parser")    
div = bs.find("div", class_="main")
#print(div)
img = div.find_all("img")
for imgs in img:
    #print(imgs.get("src"))    #拿地址
    url_src = imgs.get("src")
    img_name = url_src.split("/")[-1]   #取名字
    # 下载图片
    url_resp = requests.get(url_src)
    #url_resp.content   拿字节
    with open("img/"+img_name, mode="wb") as f:
        f.write(url_resp.content)
    print("over", img_name)
    time.sleep(1)
url_resp.close()
f.close()
print("all over!!!")

