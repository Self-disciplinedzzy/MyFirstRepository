#安装bs4    pip install bs4
from bs4 import BeautifulSoup
import requests
import csv
# 拿到数据
url = "http://www.xinsinong.com/price/list-2211.html"
resp = requests.get(url)
resp_text = resp.text
# 将生成的拿到的数据给BeautifulSoup处理，生成bs对象
page = BeautifulSoup(resp_text, "html.parser")  #警告不影响程序运行，指定html解释器
# 拿数据
# 放数据

f = open("a.csv", mode="w")
csvwriter = csv.writer(f)

data = page.find_all("li", style="float:left;width:25%")
for i in data:
    csvwriter.writerow([i.text])
resp.close()
f.close()
print("over")
