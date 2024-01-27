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
    {'ID': 'int', 'NAME': 'object', 'NEED': 'float', 'DIFF': 'float', 'GOV': 'float', 'WEA': 'float', 'GDP': 'float',
     'POP': 'float', 'URB': 'float', 'SUB': 'float', 'GEO': 'float'})
"""
NEED：需求度
DIFF：难度
GOV：行政等级
WEA：气候区
GDP：GDP
POP：人口数
URB：城镇化率
SUB：地铁里程
GEO：地质条件
"""
data_D = data_T.dropna()
print(data_D.head())

# 直接回归
y = data_D['NEED']
X = sm.add_constant(data_D[['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO']])
model1 = sm.OLS(y, X)
results1 = model1.fit()
print('\n\n——————————————直接需求回归——————————————')
print(results1.summary())

y = data_D['DIFF']
X = sm.add_constant(data_D[['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO']])
model2 = sm.OLS(y, X)
results2 = model2.fit()
print('\n\n——————————————直接难度回归——————————————')
print(results2.summary())

# 因子分析
chi_square_value, Bartlett_p = factor_analyzer.factor_analyzer.calculate_bartlett_sphericity(
    data_D.iloc[:, 4:])  # Bartlett's球状检验
kmo_all, kmo_model = factor_analyzer.factor_analyzer.calculate_kmo(data_D.iloc[:, 4:])  # KMO检验
print('\n\n——————————————Bartletts球状检验及KMO检验——————————————')
print(r"Bartlett's球状检验p值{}(标准值0.01)，KMO系数{}(标准值0.7)".format(Bartlett_p, kmo_model))
if Bartlett_p < 0.01 and kmo_model > 0.5:
    # 因子分析需要重复2次，第一次通过特征根情况判断具体需要多少个因子
    faa = factor_analyzer.FactorAnalyzer(30, rotation=None)
    faa.fit(data_D.iloc[:, 4:])
    ev, v = faa.get_eigenvalues()
    factor_num = 0
    for i in ev:
        if i > 0.9:
            factor_num = factor_num + 1
    print('\n\n——————————————特征根——————————————')
    print('特征根包括：{}，因子分析确定生成因子{}个'.format(ev, factor_num))
    print('\n\n——————————————实验方差，方差贡献比例，累计方差贡献率——————————————')
    print(faa.get_factor_variance())  # 查看方差贡献率
    # 因子分析需要重复2次，第二次固定因子数量,varimax正交旋转
    faa = factor_analyzer.FactorAnalyzer(factor_num, rotation='varimax')
    faa.fit(data_D.iloc[:, 4:])
    ev, v = faa.get_eigenvalues()  # 查看特征值ev和特征向量v
    print('\n\n——————————————成分矩阵——————————————')
    print(faa.loadings_)  # 查看成分矩阵
    print('\n\n——————————————方差，方差贡献比例，累计方差贡献率——————————————')
    print(faa.get_factor_variance())  # 查看方差贡献率
    # 特征根绘制散点图和折线图，特征根大于1表示引入的因子解释力度大于一个原始变量平均解释力度
    plt.scatter(range(1, data_D.iloc[:, 4:].shape[1] + 1), ev)
    plt.plot(range(1, data_D.iloc[:, 4:].shape[1] + 1), ev)
    plt.title("Screen Plot")
    plt.xlabel("Factors")
    plt.ylabel("Eigenvalue")
    plt.grid()  # 显示网格
    plt.show()  # 显示图形
    # 可视化展示每个隐藏变量和特征的关系
    loadings = pd.DataFrame(np.abs(faa.loadings_), index=data_D.iloc[:, 4:].columns)
    ax = sns.heatmap(loadings, annot=True, cmap="BuPu")
    ax.yaxis.set_tick_params(labelsize=15)  # 设置y轴字体大小
    plt.title("Factor Analysis", fontsize="xx-large")
    plt.ylabel("Sepal Width", fontsize="xx-large")  # 设置y轴标签
    plt.show()  # 显示图片
    # 重新构建因子表
    columns_list = ['ID', 'NAME', 'NEED', 'DIFF']
    for i in range(factor_num):
        columns_list.append('FACTOR{}'.format(i + 1))
    data_C = pd.DataFrame(faa.transform(data_D.iloc[:, 4:]))  # 转换原始数据为因子数据
    data_C = pd.concat([data_D.iloc[:, :4], data_C], axis=1)  # 拼接回原本的表头
    data_C.columns = columns_list
    print('\n\n——————————————因子提取表——————————————')
    print(data_C.head())
    # 相关性分析
    y = data_C['NEED']
    X = sm.add_constant(data_C[columns_list[4:]])
    model3 = sm.OLS(y, X)
    results3 = model3.fit()
    print('\n\n——————————————因子需求回归——————————————')
    print(results3.summary())

    y = data_C['DIFF']
    X = sm.add_constant(data_C[columns_list[4:]])
    model4 = sm.OLS(y, X)
    results4 = model4.fit()
    print('\n\n——————————————因子难度回归——————————————')
    print(results4.summary())

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
