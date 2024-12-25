import matplotlib.pyplot as plt

squares = [1, 4, 9, 25, 36]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

#设置标题并加上坐标轴的标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("树", fontsize=14)
ax.set_ylabel("平方的数", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()

