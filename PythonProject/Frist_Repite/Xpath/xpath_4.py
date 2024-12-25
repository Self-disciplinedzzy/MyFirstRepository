import requests
from lxml import etree

url = "https://www.bizhiku.net/wallpaper/car/"
resp = requests.get(url)
resp.encoding = "utf-8"
resp_text = resp.text
# print(resp_text)

html = etree.HTML(resp_text)
wallpapers = html.xpath('/html/body/ul/li/div[@class="bd"]')
# print(wallpapers)
for wallpaper in wallpapers:
    papers = wallpaper.xpath('./a/@href')
    for paper in papers:
        paperly = paper.split('/wallpaper/')[-1]
        # print(paper)
        # print(paperly)
        new_url = url + paperly
        # print(new_url)
        resp_new = requests.get(new_url)
        new_resp_text = resp_new.text
        print(new_resp_text)
        # 我在这里已经访问到了最后的一个页面，但是没血自动化点按键所以只能这样了

resp.close()
