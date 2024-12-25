import requests
# from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv

f = open("vagetables.csv", mode="w")
writer = csv.writer(f)


def download_html_page(url):
    resp = requests.get(url).text
    # # print(resp)
    # html = etree.HTML(resp)
    # txt = html.xpath("//div[@class=jxs_list price_l/text()")[0]
    # print(txt)
    page = BeautifulSoup(resp, "html.parser")
    page = page.find("div", class_="pri_k")
    txts = page.find_all("span", class_="k_1")
    names = page.find_all("span", class_="k_2")
    companies = page.find_all("span", class_="k_3")
    # LowPrices = page.find_all("span", class_="k_2")
    # HighPrices = page.find_all("span", class_="k_2")
    # print(names)
    # print(companies)
    # print(txts)
    for company in companies:
        # tet = txt.text
        # tet = txt.replace("'", "]").replace("'", "[")
        company = [company.text.replace("[", "").replace("]", "")]
        writer.writerow(company)
    for name in names:
        # tet = txt.text
        # tet = txt.replace("'", "]").replace("'", "[")
        name = [name.text.replace("[", "").replace("]", "")]
        writer.writerow(name)
    for txt in txts:
        # tet = txt.text
        # tet = txt.replace("'", "]").replace("'", "[")
        txt = [txt.text.replace("[", "").replace("]", "")]
        writer.writerow(txt)
        print(url, "over")
    # for LowPrice in LowPrices:
    #     # tet = txt.text
    #     # tet = txt.replace("'", "]").replace("'", "[")
    #     LowPrice = [LowPrice.text.replace("[", "").replace("]", "")]
    #     writer.writerow(LowPrice)
    # for HighPrice in HighPrices:
    #     # tet = txt.text
    #     # tet = txt.replace("'", "]").replace("'", "[")
    #     HighPrice = [HighPrice.text.replace("[", "").replace("]", "")]
    #     writer.writerow(HighPrice)


if __name__ == '__main__':
    for i in range(1,200):
        with ThreadPoolExecutor(50) as t:
            t.submit(download_html_page, url=f"http://www.vegnet.com.cn/Price/List_ar510000_p{i}.html?marketID=0%5d")
            # download_html_page(f"http://www.vegnet.com.cn/Price/List_ar510000_p1.html?marketID=0%5d")
