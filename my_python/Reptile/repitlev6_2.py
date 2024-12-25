from urllib import request, error

if __name__ == '__main__' :

#  url = "http://www.baiddfgdfgu.com"
    url = "http://www.baiduew.com"  # urlerror
#   url = "http://lib.cpu.edu.cn/fb/03/c1197a129795/pages.psp"   # htmlerror
    
    try:
        rep = request.Request(url) 
        rsp = request.urlopen( rep )
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))
    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))
    except Exception as e:
        print(e)
print("ok")