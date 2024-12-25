import urllib.request
import chardet
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)
    #sc = chardet.detect()
    html = rsp.read()
    html = html.decode()
    #html = html.decode(sc.get("encoding", "utf-8"))
    #print(html)