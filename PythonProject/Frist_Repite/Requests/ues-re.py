import requests 
import re


url = "https://movie.douban.com/chart"

heads = {
    "Uset-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15"
}

resp = requests.get(url, headers=heads)
print(resp.text)
'''
resp.close()
url = "https://www.16pic.com/sucai/5050348.html"
resp = requests.get(url)
resp_text = resp.text
#print(resp.text)
data = BeautifulSoup(resp_text, "html.parser")
advance_data = data.find("div", class_="flex_grid masonry").find_all("a", class_="download")
#print(advance_data)
#print(advance_data)
#print(advance_data)
for i in advance_data:
    print(i.get("href"))
'''