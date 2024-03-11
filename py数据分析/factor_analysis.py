import factor_analyzer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def pre_check(data, index, independent_varible):
    data_A = pd.concat([data.loc[:, index], data.loc[:, independent_varible]], axis=1)
    # Bartlett's球状检验
    chi_square_value, Bartlett_p = factor_analyzer.factor_analyzer.calculate_bartlett_sphericity(
        data_A.iloc[:, 1:])
    # KMO检验
    kmo_all, kmo_model = factor_analyzer.factor_analyzer.calculate_kmo(data_A.iloc[:, 1:])
    print('\n\n——————————————Bartletts球状检验及KMO检验——————————————')
    print(r"Bartlett's球状检验p值{}(需小于标准值0.01)，KMO系数{}(需大于标准值0.7)".format(Bartlett_p, kmo_model))
    return Bartlett_p, kmo_model


def analy(data, index, independent_varible, threshold=1):
    data_A = pd.concat([data.loc[:, index], data.loc[:, independent_varible]], axis=1)
    # 因子分析需要重复2次，第一次通过特征根情况判断具体需要多少个因子
    faa = factor_analyzer.FactorAnalyzer(30, rotation=None)
    faa.fit(data_A.iloc[:, 1:])
    ev, v = faa.get_eigenvalues()
    factor_num = 0
    for i in ev:
        if i > threshold:
            factor_num = factor_num + 1
    print('\n\n——————————————特征根——————————————')
    print('特征根包括：{}，因子分析确定生成因子{}个'.format(ev, factor_num))
    print('\n\n——————————————实验方差，方差贡献比例，累计方差贡献率——————————————')
    print(faa.get_factor_variance())
    # 因子分析需要重复2次，第二次固定因子数量,varimax正交旋转
    faa = factor_analyzer.FactorAnalyzer(factor_num, rotation='varimax')
    faa.fit(data_A.iloc[:, 1:])
    ev, v = faa.get_eigenvalues()  # 查看特征值ev和特征向量v
    print('\n\n——————————————成分矩阵——————————————')
    print(faa.loadings_)  # 查看成分矩阵
    print('\n\n——————————————方差，方差贡献比例，累计方差贡献率——————————————')
    print(faa.get_factor_variance())  # 查看方差贡献率
    # 特征根绘制散点图和折线图，特征根大于1表示引入的因子解释力度大于一个原始变量平均解释力度
    plt.scatter(range(1, len(ev) + 1), ev)
    plt.plot(range(1, data_A.iloc[:, 1:].shape[1] + 1), ev)
    plt.title("Screen Plot")
    plt.xlabel("Factors")
    plt.ylabel("Eigenvalue")
    plt.grid()  # 显示网格
    plt.show()  # 显示图形
    # 可视化展示每个隐藏变量和特征的关系
    loadings = pd.DataFrame(np.abs(faa.loadings_), index=data_A.iloc[:, 1:].columns)
    ax = sns.heatmap(loadings, annot=True, cmap="BuPu")
    ax.yaxis.set_tick_params(labelsize=15)  # 设置y轴字体大小
    plt.title("Factor Analysis", fontsize="xx-large")
    plt.ylabel("Sepal Width", fontsize="xx-large")  # 设置y轴标签
    plt.show()
    return factor_num, faa


def rebuild_data_for_reg(data, faa, index, independent_varible, dependent_varible, factor_names):
    columns_list = [index, dependent_varible] + factor_names
    data_C = pd.DataFrame(faa.transform(data.loc[:, independent_varible]))
    data_R = pd.concat([data.loc[:, index], data.loc[:, dependent_varible], data_C], axis=1)
    data_R.columns = columns_list
    return data_R

def rebuild_data_for_cluster(data, faa, index, independent_varible, factor_names):
    columns_list = [index] + factor_names
    data_C = pd.DataFrame(faa.transform(data.loc[:, independent_varible]))
    data_R = pd.concat([data.loc[:, index], data_C], axis=1)
    data_R.columns = columns_list
    return data_R