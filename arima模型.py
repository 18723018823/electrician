import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
# 读取数据
data = pd.read_csv('比亚迪历史数据.csv')
new_data = data['收盘'][::-1]
ts =new_data
new_data_1 = data['日期'][::-1]
ts.index = pd.to_datetime(new_data_1)

plt.figure(figsize=(10,6))
plt.plot(ts)
# 绘制时间序列图
plt.title('Stock Price Time Series')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()

# 计算自相关函数ACF和偏自相关函数PACF
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
fig, axes = plt.subplots(2,1,figsize=(10,6))
plot_acf(ts, lags=40, ax=axes[0])
plot_pacf(ts, lags=40, ax=axes[1])
plt.show()



model = ARIMA(ts, order=(10,1,3))
results = model.fit()
forecast = results.forecast(steps=180)
print(forecast)

plt.figure(figsize=(10,6))

# 绘制原始数据和预测数据的对比图
plt.plot(ts, label='Actual Price')

plt.plot(forecast, label='Predicted Price')

plt.legend()

plt.title('Actual vs. Predicted Stock Price')

plt.xlabel('Year')

plt.ylabel('Price')

plt.show()



