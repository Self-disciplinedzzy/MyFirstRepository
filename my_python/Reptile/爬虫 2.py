'''
from urllib import request, parse
if __name__ == '__main__':
    url = "https://www.baidu.com/s?   https://jstv14.cc/video/view/38aa72995a717ac3cea6 "
    wd = input("you want to kees key words:")
    
    wd_dic = {
        "wd": wd
    }
    wd_dic = parse.urlencode(wd_dic)
    fullurl = url + wd_dic
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)
'''
#在写一遍
import urllib.request
import charset
