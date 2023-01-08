"""
让用户输入一个数
利用这个数来的个数来向用户问好
"""
class Reading:
    nums = input("请你喜欢输入一个数:")     #读去数
    name = input("请你输入你的姓名:")
    def __init__(self,nums,name):
        self.nums = nums
        self.name = name
    def Read(self):

        for i in range(self.nums):
            print(f"你好{name.self},{i}")
            if nums >= 10000:
                break
Reading.Read()
