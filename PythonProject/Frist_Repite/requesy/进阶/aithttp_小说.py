# import requests
# import asyncio
# import aiohttp
# from lxml import etree


# url1 = "https://www.17k.com/list/3052783.html"
# resp = requests.get(url1)
# url2 = "https://www.17k.com"
# resp.encoding = "utf-8"
# resps = resp.text
# html = etree.HTML(resps)
# aas = html.xpath('//a[@target="_blank"]/@href')[192:-142]
# urls = []
# for a in aas:
#     urls.append(url2 + a)
# # print(urls)


# async def GetUrl(url):
#     # print(url)
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resps:
#             resps = resps.text()
#             resps.encoding='utf-8'
#             print(resps)
#             htmls = etree.HTML(resps)
#             pps = htmls.xpath('//div[@class="p"]/p/text()')
#             for p in pps:
#                 async with open("abs.txt", mode="w") as f:
#                     f.write(p)
#                     print("over", url)





# async def main():
#     tasks = []
#     for url in urls:
#         # full_url = url2 + a
#         tasks.append(asyncio.create_task(GetUrl(url)))
#         await asyncio.wait(tasks)
#     # print(tasks)




# if __name__ == '__main__':
#     asyncio.run(main())

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
aas = html.xpath('//a[@target="_blank"]/@href')[21:-20]
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
            pps = htmls.xpath('//div[@class="p"]/p/text()')
            name = url.rsplit("/")[-1] + ".txt"
            async with aiofiles.open("xiaoshuo/"+name, mode="w") as f:
                for p in pps[:-3]:
                    # print(len(p))
                    await f.write(p)
        print("over", url)


# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas




async def main():
    tasks = []
    for url in urls:
        # full_url = url2 + a
        tasks.append(asyncio.create_task(GetUrl(url)))
        await asyncio.wait(tasks)
    # print(tasks)




if __name__ == '__main__':
    asyncio.run(main())
