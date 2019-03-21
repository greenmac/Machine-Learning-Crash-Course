from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt

# print(pd.__version__)

# dataframe format
# city_name = pd.Series(['San Francisco', 'San Joes', 'Sacramento'])
# population = pd.Series([854269, 1015785, 485199])
# data_01 = pd.DataFrame({'City name':city_name, 'Population':population})
# print(data_01)

# load csv data,DataFrame.describe 来显示关于 DataFrame 的有趣统计信息
# california_housing_dataframe = pd.read_csv('https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv', sep=",")
# california_housing_dataframe_describe = california_housing_dataframe.describe()
# print(california_housing_dataframe_describe)

# 另一个实用函数是 DataFrame.head，它显示 DataFrame 的前几个记录
# california_housing_dataframe = pd.read_csv('https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv', sep=",")
# california_housing_dataframe_head = california_housing_dataframe.head()
# print(california_housing_dataframe_head)

# pandas 的另一个强大功能是绘制图表。例如，借助 DataFrame.hist，您可以快速了解一个列中值的分布
california_housing_dataframe = pd.read_csv('https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv', sep=",")
california_housing_dataframe_hist = california_housing_dataframe.hist('housing_median_age')
# print(california_housing_dataframe_hist)
plt.show()