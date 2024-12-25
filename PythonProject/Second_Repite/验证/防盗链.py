import requests
# url = "https:\/\/video.pearvideo.com\/mp4\/adshort\/20210405\/1667106437065-15648578_adpkg-ad_hd.mp4"

# 防盗链

url = "https://www.pearvideo.com/video_1725628"
cont = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={cont}&mrd=0.4996602045733768"

# print(videoStatusUrl)

headers = {

    "User-Agent": "Mozilla/5.0 (MacintoshIntel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko)",
    "Referer": url
    # 防盗链（溯源）1->2->3     本次请求的上一级是什么
}

resp = requests.get(videoStatusUrl, headers=headers)

dic = resp.json()
# 去字典里找srcurl，systemtime
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
# resp.json()['videoInfo']['videos']['srcUrl']
srcUrl = srcUrl.replace(systemTime, f"cont-{cont}")     # 替换srcurl
# print(srcUrl)
# 下载视屏

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
resp.close()

