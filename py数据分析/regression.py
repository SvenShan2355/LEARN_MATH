import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import math

# 使用清洗过的数据，pandas格式
# 参数包括：数据、索引列列名、自变量列名、变量列名
# mutiple_regression进行多元回归分析并输出结果
# simple_regression对单一自变量自身及其平方、开方、对数进行回归分析，输出四个散点图及回归结果

def mutiple_regression(data, index, independent_varible, dependent_variable):
    data_CONCAT = pd.concat([data.loc[:, index], data.loc[:, dependent_variable], data.loc[:, independent_varible]],
                            axis=1)
    print(data_CONCAT.head(10))
    y = data_CONCAT[dependent_variable]
    x = sm.add_constant(data_CONCAT[independent_varible])
    model = sm.OLS(y, x)
    results = model.fit()
    print(results.summary())


def simple_regression(data, index, independent_varible, dependent_variable):
    data_CONCAT = pd.concat([data.loc[:, index], data.loc[:, dependent_variable], data.loc[:, independent_varible]],
                            axis=1)
    # 引入平方、开方、对数三种处理方式
    quadratic=[]
    root=[]
    logarithm=[]
    for n in data_CONCAT.loc[:,independent_varible]:
        quadratic.append(n**2)
        root.append(math.sqrt(n))
        logarithm.append(math.log(n,math.e))
    data_CONCAT["quadratic"] = quadratic
    data_CONCAT["root"] = root
    data_CONCAT["logarithm"] = logarithm
    # 更改列名
    # columns_list = ['INDEX', dependent_variable, independent_varible]
    # data_CONCAT.columns = columns_list
    print(data_CONCAT.head(10))
    # 原始数据散点图
    plt.scatter(data_CONCAT[independent_varible], data_CONCAT[dependent_variable], c="red", marker='o', label='sample')
    plt.xlabel(independent_varible)
    plt.ylabel(dependent_variable)
    plt.title("raw")
    plt.legend(loc=2)
    plt.show()
    # 平方数据散点图
    plt.scatter(data_CONCAT["quadratic"], data_CONCAT[dependent_variable], c="blue", marker='o', label='sample')
    plt.xlabel("quadratic")
    plt.ylabel(dependent_variable)
    plt.title("quadratic")
    plt.legend(loc=2)
    plt.show()
    # 方根数据散点图
    plt.scatter(data_CONCAT["root"], data_CONCAT[dependent_variable], c="green", marker='o', label='sample')
    plt.xlabel("root")
    plt.ylabel(dependent_variable)
    plt.title("root")
    plt.legend(loc=2)
    plt.show()
    # 对数数据散点图
    plt.scatter(data_CONCAT["logarithm"], data_CONCAT[dependent_variable], c="black", marker='o', label='sample')
    plt.xlabel("logarithm")
    plt.ylabel(dependent_variable)
    plt.title("logarithm")
    plt.legend(loc=2)
    plt.show()
    # 多元回归检测各个变量关系
    mutiple_regression(data_CONCAT,index,[independent_varible,"quadratic","root","logarithm"],dependent_variable)
