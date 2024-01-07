import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

sales = pd.read_csv('BMWYY历史数据.csv')
new_column = sales['交易量'].str.replace('M', '') # 使用pandas.to_numeric()方法将字符串转换为数字
new_column = pd.to_numeric(new_column) # 将新列加入到DataFrame对象中
sales['交易量'] = new_column * 1000
sales['变化量']=sales['交易量']*(sales['开盘']-sales['收盘'])
print(sales['交易量'])
sales['日期'] = pd.to_datetime(sales['日期'])
sales.set_index('日期', inplace=True)
# 确定事情发生时间
identified_date = pd.to_datetime('2023-4-19')
sales_before = sales.loc[sales.index < identified_date].copy()

# 分割数据，对比事件前后的区别
sales_before_mean = sales_before['变化量'].mean()

sales_after = sales.loc[sales.index >= identified_date].copy()

sales_after_mean = sales_after['变化量'].mean()

# 数据可视化
plt.figure(figsize=(16,5))

plt.plot(sales_before.index, sales_before['变化量'], label='Before promotion')

plt.plot(sales_after.index, sales_after['变化量'], label='After promotion')

plt.axvline(x=identified_date, color='red', linestyle='--', label='Promotion date')

plt.xlabel('Date')

plt.ylabel('bianhualiang')

plt.title('before and after promotion')

plt.legend()

plt.show()
# 计算统计显著性
t_statistic, p_value = stats.ttest_ind(sales_before['变化量'], sales_after['变化量'], equal_var=False)

print(f'The t-statistic is {t_statistic:.2f} with a p-value of {p_value:.4f}')


