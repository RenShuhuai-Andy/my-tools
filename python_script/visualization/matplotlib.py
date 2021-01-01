# 官方colormap: https://matplotlib.org/tutorials/colors/colormaps.html
# 官方颜色表：https://blog.csdn.net/weixin_42643547/article/details/103683412
# 配色网站：https://colorhunt.co/palettes/popular
# 配色网站：https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3
# plt style: https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html & https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
colormap = mpl.cm.Set1.colors
plt.style.use('seaborn-whitegrid')


x = [2, 4, 6, 8]
acc = np.array([74.01736667, 74.22666, 71.2041266666666, 71.23382667])
std = np.array([3.177711758, 3.67846144283177, 4.09633922268272, 4.944713624])

# fig = plt.figure(figsize=(6, 3))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.fill_between(x, acc + std, acc - std, color=colormap[0], alpha=0.05)

imdb, = ax.plot(x, acc, color=colormap[0])

ax.scatter(x, acc, color=colormap[0])

ax.legend([imdb], [r'$|\rho|$: size of sub-policy'], loc='lower left')  # use Latex in plt
ax.set_xticks(x)
# ax.set_xlabel(r'Number of operations in one sub-policy')
ax.set_ylabel('Test Accuracy (%)')
plt.savefig(r"E:\imdb_structure.pdf", bbox_inches='tight')  # save as pdf
plt.show()