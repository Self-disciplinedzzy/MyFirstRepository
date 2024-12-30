# 安装requests
 - pip install requests
 - 国内源(清华源)
# 爬虫
  - 构造请求头
  - 带入关键字

# 正则表达式
  - . 匹配任意
  - ^ 匹配字符的开始
  - $ 匹配字符的结尾
  - 一句话提取字符
  - \d  数字  \s  空白符号  \n  换行符 \t 制表  \w  数字，字母，下划线  
  - \D  \S  \N  a|b ()  除了    或者
  - [...] 字符组 [a-zA-Z0-9]
  - [^...]  除了字符组  [^a-zA-Z0-9]
  ## 量词
    - * 匹配0次或更多次
    - + 重复一次或更多次
    - ？ 重复零次或一次
    - {n} 重复n次
    - {n,m} 重复n次到m次
    - \d(5)   匹配数字5次
    ### 贪婪匹配/惰性匹配
    - .*
    - .*?
    obj.findall(resp) 返回list
    obj.finditer(resp) 返回迭代器用for循环拿数据
    obj.march(resp) 返回march对象的结果，只返回一个结果
    obl.search(resp) 从头开始匹配找结果
    find_all
    find
    get("....")
    asdfsd.content
    csv

# xml
  - 安装  pip install lxml
  