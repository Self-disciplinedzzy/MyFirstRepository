import scrapy


class XiaoSpider(scrapy.Spider):
    name = "xiao"
    allowed_domains = ["4399.com"]
    start_urls = ["https://www.4399.com/flash"]

    def parse(self, response):
        # print(response.text)
        # print(response)
        txt = response.xpath("//ul[@class='n-game cf']/li/a/b/test()")
        print(txt)
