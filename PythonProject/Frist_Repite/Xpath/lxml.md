为什么这好用这个东西
# xpath
## 安装. pip install lxml
### 基本语法
- tree = etree.xpath("/html/*/div//a")  *表示任意一个标签
- tree = etree.xpath("/html/body/a@href)    @代表标签内的属性
- tree = etree.xpath("./body/a[1]/text()")  a[1] 在xpath里面数数从第一开始数
- tree = etree.xpath("./body/a[1]/text()")  text() 表示取标签下的文本   .表示相对路径
- 父子关系
1. xpath是XML的路径语言，用来确定XML文档中某个部分位置的语言
2.基于    XML的树状结构
""""
tree = etree.xpath("/html/ul/div//a")
print(tree) #打出来的是对象
""""