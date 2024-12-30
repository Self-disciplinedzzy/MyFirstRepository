#学习案例 更2021-10-7
#在列表之间移动元素
#先创建一个列表
#和一个用于储存的空列表
kong_lie = []
yong_lie = ["yuyue","xilan","shuijiao"]
while yong_lie:
    zhuan_lie = yong_lie.pop()
    print(f"ying dong de ci:{zhuan_lie.title()}")
    kong_lie.append(zhuan_lie)
print("zhi qian kong lie biao de:")
print(kong_lie)
for i in kong_lie:
    print("kong_lie de:")
    print(i)
    


