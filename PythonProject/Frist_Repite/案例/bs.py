from bs4 import BeautifulSoup
import requests

url = "https://www.bizhiku.net/wallpaper/car/"
resp = requests.get(url)
resp.encoding = 'utf-8'

resp_text = resp.text
# print(resp.text)

page = BeautifulSoup(resp_text, "html.parser")
imgs_url = page.find_all("div", class_="bd")


# print(imgs_url)


for img in imgs_url:
    print(img.)

resp.close()