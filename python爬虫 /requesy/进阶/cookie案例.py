import requests

url = "https://www.pearvideo.com/video_1741195"
contId = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.1229705857465615"
# print(videoStatusUrl)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15",
    "Referer": url

}

resp = requests.get(videoStatusUrl, headers=headers)
# https://video.pearvideo.com/hls/long/20210908/cont-1741195-15763654-hd.m3u8
# https://video.pearvideo.com//hls//long//20210908//1667115222077-15763654-hd.m3u8
# print(resp.text)
dic = resp.json()
print(dic)
systemTime = dic['systemTime']
srcUrl = dic['videoInfo']['videos']['srcUrl']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
# print(systemTime)
# print(srcUrl)
with open("b.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
f.close()
resp.close()