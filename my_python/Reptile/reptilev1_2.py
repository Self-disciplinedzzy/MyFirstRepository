from urllib import request
if __name__ == '__main__':
    url = "https://weather.com/zh-CN/weather/today/l/30.37,113.46?par=apple_widget"
    rsp = request.urlopen(url)
    html = rsp.read()
    print(type(html))
    html = html.decode()
    #需要解决编码问题
    #安装chardet        pip install chardet
    print(html)
    





