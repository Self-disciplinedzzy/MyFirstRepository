import asyncio
import time


async def func1():
    print("李雪琴")
    await asyncio.sleep(1)
    print("李雪琴")


async def func2():
    print("秦霄贤")
    await asyncio.sleep(5)
    print("秦霄贤")


async def func3():
    print("郭德纲")
    await asyncio.sleep(3)
    print("郭德纲")


async def main():
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)
if __name__ == '__main__':

    t1 = time.time()

    asyncio.run(main())

    t2 = time.time()

    t = t2 - t1
    print(t)
