# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # 利用网格来创建子图，可以单独调整子图大小

file = r"C:\Users\Administrator\Desktop\LSCQ.xlsx"
data = pd.read_excel(file)
data_T = data.astype(
    {'ID': 'int', 'NAME': 'object', 'NEED': 'float', 'DIFF': 'float', 'GOV': 'float', 'WEA': 'float', 'GDP': 'float',
     'POP': 'float', 'URB': 'float', 'SUB': 'float', 'GEO': 'float'})

da_L = data_T.values
propname = ['行政等级', '气候', 'GDP', '人口', '城镇化率', '地铁里程', '地址条件']
fig = plt.figure(figsize=(5, 120), dpi=100)  # 设置图形的大小
grid = gridspec.GridSpec(24, 1)  # 设定4行*2列的网格

for k in range(len(da_L)):
    print(k)
    propvalue = []
    propvalue1 = da_L[k][4:].tolist()
    for num in propvalue1:
        round_num = round(num, 2)
        propvalue.append(round_num)
    name = da_L[k].tolist()[1]

    angles = np.linspace(0, 2 * np.pi, len(propname), endpoint=False)  # np.linspace() 用于在指定的起始点和结束点之间生成等间隔的数值序列
    angles_a = np.concatenate((angles, [angles[0]]))  # np.concatenate()用来对数列或矩阵进行合并

    propvalue1_a = propvalue + [propvalue[0]]

    ax = fig.add_subplot(grid[k, 0], polar=True)  # 创建一个子图，第一行第一列给第1个子图（可以用切片将多于一行一列给一个子图）
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 显示负号

    ax.plot(angles_a, propvalue1_a, color='r')  # 绘制折线图，在极坐标下仍然使用plot()，只需参数是极坐标参数（第一个参数为角度，第二个参数为距离）就可以
    ax.fill(angles_a, propvalue1_a, color='b', alpha=0.2)  # 填充区域

    for item in range(len(propname)):  # 把具体的值显示在图上，text在极坐标上一样用，只是前两个参数是极坐标（第一个参数为角度，第二个参数为距离）
        ax.text(angles_a[item], propvalue1_a[item], s=propvalue1_a[item])

    plt.thetagrids(angles * 180 / np.pi, propname, color="c", fontsize=10)  # 设置网格标签，第一个参数的单位需由弧度转化成度数
    ax.tick_params(pad=10, grid_color='k', grid_alpha=0.2, grid_linewidth=1, grid_linestyle=(0, (5, 5)), labelsize=10,
                   labelcolor="k")
    """
    pad 刻度线和刻度值之间的距离
    labelsize 刻度值的字体大小。注意这个地方的labelsize会把上面thetagrids的fontsize覆盖
    labelcolor 刻度值的文字颜色
    grid_alpha 网格线透明度
    grid_color 网格线颜色
    grid_linewidth 网格线宽度
    grid_linestyle 网格线型
    """
    ax.set_theta_zero_location('N')  # 设置0度起始位置
    ax.set_rlabel_position(270)  # 设置坐标值显示角度相对于起始角度的偏移量
    ax.set_rlim(0, 10)  # 设置显示的极径范围
    ax.set_rmax(10)  # 设置显示的极径最大值
    ax.set_rticks(np.arange(1, 10, 1))  # 设置极径网格线的显示范围
    ax.set_theta_direction(-1)  # 设置坐标轴正方向，默认逆时针

    ax.set_title(name, y=-0.3, fontsize=12)  # 设置标题

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.3, hspace=0.9)
plt.savefig("jizuobiao")
