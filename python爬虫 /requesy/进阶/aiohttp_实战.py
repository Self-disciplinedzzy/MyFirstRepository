# 今天来测试一下性能

import aiohttp
import asyncio

urls = [
    "http://img.netbian.com/file/2022/1031/231454oP9Cb.jpg",
    "http://img.netbian.com/file/20111224/b1068e88da983629f1b36a4e268cd021.jpg",
    "http://img.netbian.com/file/2022/1030/234433MXoYX.jpg",
    "http://img.netbian.com/file/2022/0918/235032Kwy4J.jpg"
    "http://img.netbian.com/file/2022/1026/002806DHEDn.jpg",
    "http://img.netbian.com/file/2022/0918/1349140jMnt.jpg",
    "https://img.bizhiku.net/uploads/2022/0730/iqcqyjken1u.jpg",
    "https://img.bizhiku.net/uploads/2022/0730/f1vwzmq3jyh.jpg",
    "https://img.bizhiku.net/uploads/2022/0812/aghgxe0fuur.jpg",
    "https://img.bizhiku.net/uploads/2022/0731/ryyjyqbcvbv.jpg",
    "https://img.bizhiku.net/uploads/2020/0519/ouqz5t0o05p.jpg",
    "https://img.bizhiku.net/uploads/2022/0731/cvxzqngitvy.jpg",
    "https://img.bizhiku.net/uploads/2022/0202/ex4jmyfuxdu.jpg",
    "https://img.bizhiku.net/uploads/2022/0730/tdmwz3qzmwe.jpg",
    "https://img.bizhiku.net/uploads/2022/0625/v5xroqgf4rz.jpg",
    "https://img.bizhiku.net/uploads/2021/0807/5zsexwn1apc.jpg",
    "https://img.bizhiku.net/uploads/2021/1208/zwtgcgwsoua.jpg",
    "https://img.bizhiku.net/uploads/2022/0809/yx4tcgdrhqd.jpg",
    "https://img.bizhiku.net/uploads/2022/0626/qm01xrq2uup.jpg",

]
async def aiodownload(url):
    # 访问，拿东西
    name = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open("wp/"+name, mode="wb") as f:
                f.write(await resp.content.read())
    print(url, "搞定")
async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())