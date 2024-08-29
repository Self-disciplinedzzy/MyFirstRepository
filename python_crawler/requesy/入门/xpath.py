import time
from lxml import etree
import requests

url = "https://pic.netbian.com"
for i in range(1, 7):
    a = f"index_{i}"
    full_url = url + a
    print(full_url)    
resp = requests.get(url)
resp.encoding = "gbk"
resp_text = resp.text
    # print(resp_text)
html = etree.HTML(resp_text)
imgs = html.xpath("/html/body//img/@src")
for img in imgs:
    print(img)
    img_resp = requests.get(img)
    img_data = img_resp.content
    img_name = img.split("/")[-1]
    time.sleep(1)
    with open(img_name, mode="wb") as f:
        f.write(img_data)
        
    print("over")
img_resp.close()
print("all over!!!")