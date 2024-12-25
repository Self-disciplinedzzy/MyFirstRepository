from lxml import etree
import requests
import time


url = "https://www.woyaogexing.com/shouji/"

# for i in range(1,7):

    # urls = url + "index_" + str(i)

resp = requests.get(url)
resp.encoding = "utf-8"
resp_text = resp.text
# print(resp_text)
html = etree.HTML(resp_text)

divs = html.xpath("/html/body/div[3]/div[3]/div[1]/div[2]/div")
https = "https:"

for div in divs:
    img = div.xpath("./a/img/@src")
    # print("".join(img))
    img_pro = "".join(img)
    full_img = https + img_pro
    resp_img = requests.get(full_img)
    resp_name = full_img.split("/")[-1]
    with open("img/"+resp_name, mode="wb") as f:
        f.write(resp_img.content)
        print("over", resp_name)
        time.sleep(1)
resp_img.close()
f.close()
print("over!!!")
