import csv
import requests
from lxml import etree
url = "https://xiantao.zbj.com/sem/index?pmcode=130719304&utm_source=bdpz&utm_medium=SEM"

# 拿到网页源代码
resp = requests.get(url)
resp_text = resp.text
# print(resp)

# 解析数据
html = etree.HTML(resp_text)
totals = html.xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div')
# print(total)

f = open("b.csv", mode="w")
writer_csv = csv.writer(f)
for total in totals:
    company_names = total.xpath('./a/span//text()')
    print(company_names)

    # moneys = total.xpath('./a/span/span/text()')
    # # print(company_name)
    for company_name in company_names:
        # print(company_name)
        writer_csv.writerow([company_name])
