from threading import Thread

# def lei():
# for i in range(90):
# print("lei", i)

# if __name__ == "__main__":
# 一定要记住这个表达方式&老师讲的不同
# t = threading.Thread(target=lei)   # 创建县城并告诉需要开哪一个任务的县城
# t.start()   # 开始县城（只是一个状态，还得看CPU）
# for i in range(100):
#     print("main", i)



# 另一种表示方法
class Mythread(Thread):
    def run(self):
        for i in range(100):
            print("run", i)


if __name__ == '__main__':
    t = Mythread()
    
    t.start()

    for i in range(100):
        print("main", i)
