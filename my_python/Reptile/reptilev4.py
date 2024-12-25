from urllib import request, parse
if __name__ == '__main__':

    #不知道为什么百度搜索栏里的和大拿的不一样
    url = 'http://www.baidu.com/s?'
    
    wd = input("请输入你要搜索的关键字:")
    
    qs = {
        "wd" : wd
    }

    print(qs)
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = url + qs
    
    rsp = request.urlopen(fullurl)

    html = rsp.read()
    html = html.decode()
    print(html)