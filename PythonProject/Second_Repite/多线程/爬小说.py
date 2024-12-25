# from lxml import etree
# import requests
# import aiohttp
# import asyncio
# import aiofiles
# # 拿a标签的网址.拼起来，再访问
# # requests不用异步
# # 爬小说内容需要异步
# # async def fangwen(url):
# # url1 = "https://www.17k.com/list/3052783.html"
# # # https://www.17k.com/chapter/3052783/38805285.html
# # resp1 = requests.get(url1)
# # resp1.encoding = 'utf-8'
# # resp_text = resp1.text
# # # print(resp_text)
# # html = etree.HTML(resp_text)
# # aas = html.xpath('//a[@target="_blank"]/@href')[22:-17]
# # url2 = "https://www.17k.com"

# # async def GetUrl(fullurl):
# #     for a in aas:
# #         fullurl = url2 + a
# #         async with aiohttp.ClientSession() as session:
# #             async with session.get(fullurl) as resp2:
# #                 html2 = etree.HTML(resp2)
# #                 ps = html2.xpath('.//div[@class="p"]/p/text()')
# #                 async with aiofiles.open("xaioshu.txt", mode="w") as f:
# # await f.write(p)
# # 用来拿到文件,下载文件


# async def GetUrl(fullurl):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(fullurl) as resps:
#             html1 = etree.HTML(resps)
#             ps = html1.xpath('.//div[@class="p"]/p/text()')


# async def download(ps):
#     async with aiofiles.open("xs.txt", mode="w") as f:
#         for p in ps:
#             await f.write(p)


# if __name__ == '__main__':
#     url2 = "https://www.17k.com"
#     url1 = "https://www.17k.com/list/3052783.html"
#     # https://www.17k.com/chapter/3052783/38805285.html
#     resp1 = requests.get(url1)
#     resp1.encoding = 'utf-8'
#     resp_text = resp1.text
#     # print(resp_text)
#     html = etree.HTML(resp_text)
#     aas = html.xpath('//a[@target="_blank"]/@href')[22:-17]
#     fullurls = url2 + aas
#     for fullurl in fullurls:


import requests
import asyncio
import aiohttp
import aiofiles
from lxml import etree


url1 = "https://www.17k.com/list/3052783.html"
resp = requests.get(url1)
url2 = "https://www.17k.com"
resp.encoding = "utf-8"
resps = resp.text
html = etree.HTML(resps)
aas = html.xpath('//a[@target="_blank"]/@href')[22:-22]
urls = []
for a in aas:
    urls.append(url2 + a)
# print(urls)


async def GetUrl(url):
    # print(url)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as resps:
            resps = await resps.text()
            # print(resps)
            htmls = etree.HTML(resps)
            pps = htmls.xpath('//div[@class="p"]/p/text()')[:-4]
            name = url.rsplit("/")[-1]
            # print(name)
            async with aiofiles.open("asdf/"+name, mode="w") as f:
                # await f.write(pps)
                for p in pps:
                    await f.write(p)
            print("over", url)


async def main():
    tasks = []
    for url in urls:
        # full_url = url2 + a
        tasks.append(asyncio.create_task(GetUrl(url)))
        await asyncio.wait(tasks)
    # print(tasks)


if __name__ == '__main__':
    asyncio.run(main())
