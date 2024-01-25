import numpy as np
import pandas as pd
import factor_analyzer
import statsmodels.api as sm
from shapely import geometry
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 读取及清洗数据
file = r"C:\Users\Administrator\Desktop\LSCQ.xlsx"
data = pd.read_excel(file)
data_T = data.astype(
    {'ID': 'int', 'NAME': 'object', 'XZ_LV': 'float', 'GDP': 'float', 'GM_LV': 'float', 'POP': 'float', 'URB': 'float',
     'LINE': 'float'})
data_D = data_T.dropna()
print(data_D.head())

# 因子分析
chi_square_value, Bartlett_p = factor_analyzer.factor_analyzer.calculate_bartlett_sphericity(
    data_D.iloc[:, 2:])  # Bartlett's球状检验
kmo_all, kmo_model = factor_analyzer.factor_analyzer.calculate_kmo(data_D.iloc[:, 2:])  # KMO检验
print(r"Bartlett's球状检验p值{}(标准值0.01)，KMO系数{}(标准值0.7)".format(Bartlett_p, kmo_model))
if Bartlett_p < 0.01 and kmo_model > 0.5:
    # 因子分析需要重复2次，第一次通过特征根情况判断具体需要多少个因子，第二次固定因子数量,varimax正交旋转
    faa = factor_analyzer.FactorAnalyzer(3,rotation='varimax')
    faa.fit(data_D.iloc[:, 2:])
    ev, v = faa.get_eigenvalues() # 查看特征值ev和特征向量v
    print(faa.loadings_) # 查看成分矩阵
    print(faa.get_factor_variance()) # 查看因子贡献率
    # 特征根绘制散点图和折线图，特征根大于1表示引入的因子解释力度大于一个原始变量平均解释力度
    plt.scatter(range(1, data_D.iloc[:, 2:].shape[1] + 1), ev)
    plt.plot(range(1, data_D.iloc[:, 2:].shape[1] + 1), ev)
    plt.title("Screen Plot")
    plt.xlabel("Factors")
    plt.ylabel("Eigenvalue")
    plt.grid()  # 显示网格
    plt.show()  # 显示图形
    # 可视化展示每个隐藏变量和特征的关系
    loadings = pd.DataFrame(np.abs(faa.loadings_), index=data_D.iloc[:, 2:].columns)
    ax = sns.heatmap(loadings, annot=True, cmap="BuPu")
    ax.yaxis.set_tick_params(labelsize=15) # 设置y轴字体大小
    plt.title("Factor Analysis", fontsize="xx-large")
    plt.ylabel("Sepal Width", fontsize="xx-large") # 设置y轴标签
    plt.show() # 显示图片

    data_C = pd.DataFrame(faa.transform(data_D.iloc[:, 2:]))# 转换原始数据为因子数据
    data_C = pd.concat([data_D.iloc[:,:2], data_C], axis=1) # 拼接回原本的表头
    data_C.columns = ['ID','NAME','FACTOR1','FACTOR2','FACTOR3']
    print(data_C.head())

# 相关性分析
y = data_C['FACTOR3']
X = sm.add_constant(data_C[['FACTOR1', 'FACTOR2']])
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

# 空间相关分析
# shapely模块介绍 https://blog.csdn.net/weixin_44374471/article/details/111821617
# geopandas模块介绍 https://zhuanlan.zhihu.com/p/554139339

# contents = [(loc, 0.5) for loc in range(0, 10, 2)]
# geo_df = gpd.GeoDataFrame(data=contents,
#                           geometry=[geometry.MultiPoint(np.random.normal(loc=loc, scale=scale, size=[10, 2]).tolist())
#                                     for loc, scale in contents],
#                           columns=['均值', '标准差'])
#
# print(geo_df)
