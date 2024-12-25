import requests

url = "https://img.bizhiku.net/uploads/2022/0730/iqcqyjken1u.jpg"
resp = requests.get(url)
name = url.split("/")[-1]
with open(name, mode="wb") as f:
    f.write(resp.content)
print("over", name)