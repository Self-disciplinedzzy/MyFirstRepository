import urllib.request
import chardet
if __name__ == '__main__':
    url = 'https://www.pythonheidong.com/blog/article/807979/858483d0d4f406c9cd47/'
    #关于为什么sometimes会  模块'urllib'没有属性'请求'
    rsp = urllib.request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    print(type(html))
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)
