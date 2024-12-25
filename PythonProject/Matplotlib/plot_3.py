import matplotlib.pyplot as plt

plt.style.use('seaborn')
input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#设置标题并加上坐标轴的标签
ax.set_title("suquare_mun", fontsize=24)
ax.set_xlabel("mun", fontsize=14)
ax.set_ylabel("suquare", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
