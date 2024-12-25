from multiprocessing import Process


def func():
    for i in range(100):
        print("紫荆城", i)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    for i in range(100):
        print("主劲程", i)
