alien_0 = {'color': 'green', 'speed': 5}
# print(alien_0['poinst'])
# 如果get方法第二个没有传参数，终端就返回None

point_value = alien_0.get('point', "No point value")
print(point_value)
