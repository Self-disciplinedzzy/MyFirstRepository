from threading import Thread


def func(name):
    for i in range(100):
        print(name, i)


if __name__ == '__main__':
    t1 = Thread(target=func, args=("挖掘机",))
    t1.start()

    t2 = Thread(target=func, args=("张耀扬",))
    t2.start()

    for i in range(100):
        print("主线程", i)
