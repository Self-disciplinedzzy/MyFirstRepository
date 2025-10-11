cars = ["bmw", "audi", "toyata", "subaru"]
cars.sort(reverse=True)
# reverse=反向
cars.sort()
# 按字母顺序排列
print(cars)
print("Here is the original list:")
print(cars)
# 用sorted()临时排列列表
print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)
# reverse方法只是反转列表
cars.reverse()
print(cars)

cars.reverse()
print(cars)
print(len(cars))