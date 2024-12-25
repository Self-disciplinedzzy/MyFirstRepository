 import requests

# url = "https://www.17k.com"
# resp = requests.get(url)
# resp.encoding="utf-8"
# print(resp.text)

# url = "https://www.17k.com"
url = "https://passport.17k.com/ck/user/login"
session = requests.session()
data = {
    "loginName": "17371733661",
    "password": "zhang66666"
}
resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)  # 看不懂
# 抓包工具里面的cookie： Set-Cookie: accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F10%252F50%252F19%252F99291950.jpg-88x88%253Fv%253D1667061960000%26id%3D99291950%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BY6f6y6r0u%26e%3D1682657470%26s%3D474374a3b0bfe4c6; expires=Fri, 28-Apr-2023 04:51:10 GMT; Max-Age=15552000; path=/; domain=17k.com   一毛一样


resp_1 = session.get(
    "https://user.17k.com/ck/user/myInfo/99291950?bindInfo=1&appKey=2406394919")

print(resp_1.json())
