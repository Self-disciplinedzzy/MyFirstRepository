dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 元组可以被重新定义
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
# 不可变的列表是元祖
# demesions[0] = 100
print(dimensions)

# 如果创建的元组只有一个元素,那就要加逗号
one_dimension = (3,)
print(one_dimension)