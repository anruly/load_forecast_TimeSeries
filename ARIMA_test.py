import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller as ADF

# 参数初始化
discfile = 'D:/GitHub/load_forecast_TimeSeries/data/arima_data.xls'

# 读取数据，指定日期列为指标，Pandas自动将“日期”列识别为Datetime格式
data = pd.read_excel(discfile, index_col=0)
# print(data.head())
# print('\n Data Type:')
# print(data.dtypes)

# 绘制时间序列图
'''
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
data.plot()
plt.show()
'''

# 自相关图
# plot_acf(data)
# plt.show()
'''
由自相关图可以看出，在4阶后才落入区间内，并且自相关系数长期大于零，显示出很强的自相关性
'''

# 平稳性检验
# print(u'原始序列的ADF检验结果为:', ADF(data[u'销量']))
# 返回值依次为adf、pvalue、usedlag、nobs、critical values、icbest、regresults、resstore
# 从返回值看检验结果的pvalue即p值显著大于0.05，判断该序列为非平稳序列。

# 时间序列的差分d
D_data = data.diff().dropna()
D_data.columns = [u'销量差分']
# D_data.plot()  # 时序图
# plt.show()

# 差分后序列自相关检验
# plot_acf(D_data)
# plt.show()

# 差分后偏自相关检验
from statsmodels.graphics.tsaplots import plot_pacf

# plot_pacf(D_data)
# plt.show()

# 差分后序列平稳性检验
# print(u'差分序列的ADF检验结果为：',ADF(D_data[u'销量差分']) )

# 平稳性检验通过，还需要进行白噪声检验
from statsmodels.stats.diagnostic import acorr_ljungbox

# print(u'差分序列的白噪声检验结果为:', acorr_ljungbox(D_data, lags=1))
# 返回统计量和p值

# 比较一阶差分和二阶差分序列
# # 一阶差分
# fig = plt.figure(figsize=(12, 8))
# ax1 = fig.add_subplot(121)
# diff1 = data.diff(1)
# diff1.plot(ax=ax1)
# # 二阶差分
# ax2 = fig.add_subplot(122)
# diff2 = data.diff(2)
# diff2.plot(ax=ax2)
# plt.show()

# 合适的p、q
import statsmodels.api as sm

dta = data.diff(1)[1:]
# print(dta)

fig = plt.figure(figsize=[12, 8])
ax1 = fig.add_subplot(211)
fig1 = sm.graphics.tsa.plot_acf(dta[u'销量'], lags=10, ax=ax1)
ax2 = fig.add_subplot(212)
fig2 = sm.graphics.tsa.plot_pacf(dta[u'销量'], lags=10, ax=ax2)
plt.show()

# 预测
predict_sunspots =

