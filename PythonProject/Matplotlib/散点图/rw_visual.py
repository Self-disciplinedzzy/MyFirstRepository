import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个实例
rw = RandomWalk()
rw.fill_walk()
# 绘制点
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
# plt.savefig('quuares_plot.png', bbox_inches='tight')