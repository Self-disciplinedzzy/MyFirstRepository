import threading
def text():
    for i in range(89):
        print("most", i)

if __name__ == "__main__":
    t = threading.Thread(target=text)
    t.start()
    for i in range(90):
        print(i)