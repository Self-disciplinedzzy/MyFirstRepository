import urllib.request
import chardet
if __name__ == '__main__':
    url = 'https://www.pythonheidong.com/blog/article/807979/858483d0d4f406c9cd47/'
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)
    
    #查看html的头号数据

    print("URL: {0}".format(rsp.geturl()))
    print("INFO: {0}".format(rsp.info()))

    print("Code: {0}".format(rsp.getcode()))
    print("试用快捷键")
    html = rsp.read()
    html = html.decode()
