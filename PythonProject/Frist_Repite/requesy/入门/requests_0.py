from urllib.request import urlopen
url = "http://www.baidu.com"

resp = urlopen(url)
with open("mybaidu.html", mode="w", encoding="utf-8") as w :
    w.write(resp.read().decode("utf-8"))

resp.close()
print("over")