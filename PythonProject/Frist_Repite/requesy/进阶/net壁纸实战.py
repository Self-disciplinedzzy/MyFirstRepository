import requests
from bs4 import BeautifulSoup
url = "https://pic.netbian.com"
resp = requests.get(url).content
# resp.encoding = 'gbk'
# <ul class="clearfix">
# img
page = BeautifulSoup(resp, "html.parser")
ullist = page.find("ul", class_="clearfix").find_all("img")
print(ullist)
for ul in ullist:
    src = ul.get("src")
    new_url = "https://pic.netbian.com" + src
    # print(new_url)
    pic_resp = requests.get(new_url).content
    pic_name = src.split("/")[-1]
    print(pic_name)
    with open("img/" +pic_name, mode="wb") as f:
        f.write(pic_resp)
    print("over!!!", src)
print("all over!!!")

