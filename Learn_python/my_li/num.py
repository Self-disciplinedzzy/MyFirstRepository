"""
让用户输入一个数
利用这个数来的个数来向用户问好
"""


class Reading:
    def __init__(self, nums, name):
        self.nums = nums
        self.name = name.title()

    def Read(self):
        for i in range(int(self.nums)):
            print(f"Hello my friend,{self.name},the number you like is {i}.")
            if int(self.nums) >= 10000:
                break


nums = input("请你喜欢输入一个数:")  # get nums
name = input("请你输入你的姓名:")  # get name

Reading(nums, name).Read()
