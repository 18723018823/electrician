import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

sales = pd.read_csv('BMWYY历史数据.csv')
new_column = sales['交易量'].str.replace('K', '') # 使用pandas.to_numeric()方法将字符串转换为数字
new_column = pd.to_numeric(new_column) # 将新列加入到DataFrame对象中
sales['交易量'] = new_column * 1000
sales['变化量']=sales['交易量']*(sales['开盘']-sales['收盘'])
print(sales['交易量'])
sales['日期'] = pd.to_datetime(sales['日期'])

sales.set_index('日期', inplace=True)

identified_date = pd.to_datetime('2023-4-19')

sales_before = sales.loc[sales.index < identified_date].copy()

sales_after = sales.loc[sales.index >= identified_date].copy()

before_mean = sales_before['变化量'].mean()

after_mean = sales_after['变化量'].mean()

plt.figure(figsize=(16,5))

plt.plot(sales_before.index, sales_before['变化量'], label='Before promotion')

plt.plot(sales_after.index, sales_after['变化量'], label='After promotion')

plt.axvline(x=identified_date, color='red', linestyle='--', label='Promotion date')

plt.xlabel('Date')

plt.ylabel('bianhualiang')

plt.title('Sales before and after promotion')

plt.legend()

plt.show()

F_statistic, p_value = f_oneway(sales_before['变化量'], sales_after['变化量'])

print(f'The F-statistic is {F_statistic:.2f} with a p-value of {p_value:.4f}')

