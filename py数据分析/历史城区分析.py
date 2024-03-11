import pandas as pd
import matplotlib.pyplot as plt
import regression
import factor_analysis
import cluster

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

# # 直接回归
# print('\n\n——————————————直接需求回归——————————————')
# regression.mutiple_regression(data_D, "NAME", ['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO'], 'NEED')
# regression.mutiple_regression(data_D, "NAME", ['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO'], 'DIFF')

# 因子分析
Bartlett_p, kmo_model = factor_analysis.pre_check(data_D, "NAME", ['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO'])
if Bartlett_p < 0.01 and kmo_model > 0.5:
    factor_num, faa = factor_analysis.analy(data_D, "NAME", ['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO'])
    # data_NEED = factor_analysis.rebuild_data_for_reg(data_D, faa, "NAME",
    #                                                  ['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO'],
    #                                                  'NEED', ["FACTOR1", "FACTOR2", "FACTOR3"])
    # data_DIFF = factor_analysis.rebuild_data_for_reg(data_D, faa, "NAME",
    #                                                  ['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO'],
    #                                                  'DIFF', ["FACTOR1", "FACTOR2", "FACTOR3"])
    # regression.mutiple_regression(data_NEED, "NAME", ["FACTOR1", "FACTOR2", "FACTOR3"], "NEED")

# 聚类分析
data_C = factor_analysis.rebuild_data_for_cluster(data_D, faa, "NAME",
                                                  ['GOV', 'WEA', 'GDP', 'POP', 'URB', 'SUB', 'GEO'],
                                                  ["FACTOR1", "FACTOR2", "FACTOR3"])

cluster.pre_check(data_C)


# 空间相关分析
# shapely模块介绍 https://blog.csdn.net/weixin_44374471/article/details/111821617
# geopandas模块介绍 https://zhuanlan.zhihu.com/p/554139339
