import requests

url = "https://www.pearvideo.com/video_1694276"
contId = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5270696699285751"
# print(videoStatusUrl)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15",
    "Referer": url
}
resp = requests.get(videoStatusUrl, headers=headers)

dic = resp.json()
# print(dic)
systemTime = dic['systemTime']
srcUrl = dic['videoInfo']['videos']['srcUrl']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
# print(srcUrl)  
# print(systemTime)
# print(srcUrl)

with open("b.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

f.close()

resp.close()