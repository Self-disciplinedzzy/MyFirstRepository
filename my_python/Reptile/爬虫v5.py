from urllib import request, parse
import json
baseurl = "http://fanyi.baidu.com/sug"

data = {
    'kw': 'girl'
}

data = parse.urlencode(data).encode('utf-8')
print(type(data))

headers = {
    'Content-Length':len(data)
}

rsp = request.urlopen(baseurl, data=data)

mkdir -p ~/.vim/tools/pydiction
cp -r pydiction-master/after ~/.vim
cp pydiction-master/complete-dict ~/.vim/tools/pydiction
