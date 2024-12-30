#学习案例 更2021-10-7
#删除列表里的特定值
#先创建一个列表
xian_lie = ["car","feiji","car","houche","car","moyong","car","car"]
#删除里面的car
print(xian_lie)
while "car" in xian_lie:
    xian_lie.remove("car")

print(xian_lie)
