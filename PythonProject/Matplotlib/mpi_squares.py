import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

ax.set_title("平方数", fontsize=24)
ax.set_ylabel("值的平方", fontsize=12)
ax.set_xlabel("值", fontsize=12)


# 刻度尺大小
ax.tick_params(axis='both', labelsize=14)


plt.show()
