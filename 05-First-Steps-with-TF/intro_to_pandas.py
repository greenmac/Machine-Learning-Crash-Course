from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
import ssl
import numpy as np

ssl._create_default_https_context = ssl._create_unverified_context
# print(pd.__version__)

"""
basic concept
"""
## dataframe format
city_name = pd.Series(['San Francisco', 'San Joes', 'Sacramento'])
population = pd.Series([854269, 1015785, 485199])
cities = pd.DataFrame({'City name':city_name, 'Population':population})
# print(cities)

# load csv data,DataFrame.describe 来显示关于 DataFrame 的有趣统计信息
# california_housing_dataframe_describe = california_housing_dataframe.describe()
# print(california_housing_dataframe_describe)

# 另一个实用函数是 DataFrame.head，它显示 DataFrame 的前几个记录
california_housing_dataframe = pd.read_csv('https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv', sep=",")
# california_housing_dataframe_head = california_housing_dataframe.head()
# print(california_housing_dataframe_head)

## pandas 的另一个强大功能是绘制图表。例如，借助 DataFrame.hist，您可以快速了解一个列中值的分布
# california_housing_dataframe_hist = california_housing_dataframe.hist('housing_median_age')
# plt.show()

"""
Access data
"""
## print data
cities = pd.DataFrame({'City name':city_name, 'Population':population})
# print(type(cities['City name']))
# print(cities['City name'])
# print(type(cities['City name'][1]))
# print(cities['City name'][1])
# print(type(cities[0:1]))
# print(cities[0:2])

"""
Manipulating data
"""
## basic command
# print(population/1000)
## numpy
# print(np.log(population))
## apply
# print(population.apply(lambda val:val>1000000))
## modify
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
# print(cities)

"""
practice01
通过添加一个新的布尔值列（当且仅当以下两项均为 True 时为 True）修改 cities 表格：

城市以圣人命名。
城市面积大于 50 平方英里。
注意：布尔值 Series 是使用“按位”而非传统布尔值“运算符”组合的。例如，执行逻辑与时，应使用 &，而不是 and。

提示："San" 在西班牙语中意为 "saint"。
"""
cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name:name.startswith('San'))
# print(cities)

"""
index
"""
city_name_index = city_name.index
# print(city_name_index)
cities_index = cities.index
# print(cities_index)
cities_reindex = cities.reindex([2, 0, 1])
# print(cities_reindex)
cities_random_permutation = cities.reindex(np.random.permutation(cities.index))
# print(cities_random_permutation)

"""
practice02
reindex 方法允许使用未包含在原始 DataFrame 索引值中的索引值。请试一下，看看如果使用此类值会发生什么！您认为允许此类值的原因是什么？
这种行为是可取的，因为索引通常是从实际数据中提取的字符串(顯示NaN)
"""
cities_reindex_02 = cities.reindex([0, 4, 5, 2])
print(cities_reindex_02)
