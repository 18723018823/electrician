import pandas as pd
import numpy as np
import talib
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def calculate_technical_indicators(future_df,df): # 计算移动平均线
    future_df["MA5"] = df["收盘"].rolling(window=5).mean()
    future_df["MA10"] = df["收盘"].rolling(window=10).mean()
    # 计算相对强弱指数（RSI）
    delta = df["收盘"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    future_df["RSI"] = 100 - (100 / (1 + rs))
    future_df["RSI_1"] = 100 - (100 / (1 + rs))
    future_df["RSI_2"] = 100 - (100 / (1 + rs))
    return future_df.dropna()

df = pd.read_csv('比亚迪历史数据.csv')
new_column = df['交易量'].str.replace('M', '') # 使用pandas.to_numeric()方法将字符串转换为数字
new_column = pd.to_numeric(new_column) # 将新列加入到DataFrame对象中
df['交易量'] = new_column * 1000000
new_column = df['涨跌幅'].str.replace('%', '') # 使用pandas.to_numeric()方法将字符串转换为数字
new_column = pd.to_numeric(new_column) # 将新列加入到DataFrame对象中
df['涨跌幅'] = new_column / 100
close = df['收盘'].values # 计算技术指标
ma_5 = talib.SMA(close, timeperiod=5) # 5日移动平均线
ma_20 = talib.SMA(close, timeperiod=20) # 20日移动平均线
std_20 = talib.STDDEV(close, timeperiod=20) # 20日收盘价标准差
rsi_14 = talib.RSI(close, timeperiod=14) # 14日相对强弱指标(RSI)
adx_14 = talib.ADX(df['高'], df['低'], close, timeperiod=14) # 14日平均趋向指数(ADX) # 将各项指标组合成一个特征矩阵
mean_value = np.nanmean(ma_20[-180:])
ma_20[-180:][np.isnan(ma_20[-180:])] = mean_value

mean_value = np.nanmean(std_20[-180:])
std_20[-180:][np.isnan(std_20[-180:])] = mean_value

mean_value = np.nanmean(ma_5[-180:])
ma_5[-180:][np.isnan(ma_5[-180:])] = mean_value

mean_value = np.nanmean(rsi_14[-180:])
rsi_14[-180:][np.isnan(rsi_14[-180:])] = mean_value

mean_value = np.nanmean(adx_14[-180:])
adx_14[-180:][np.isnan(adx_14[-180:])] = mean_value

X = np.column_stack((ma_5[-180:], ma_20[-180:], std_20[-180:], rsi_14[-180:], adx_14[-180:])) # 构建线性回归模型
print(X)
print(ma_20[-180:])
print(ma_5[-180:])
print(std_20[-180:])
print(rsi_14[-180:])

model = LinearRegression()
model.fit(X[:-1], close[-142:])

y_pred = model.predict(X) # 绘制图形
plt.plot(df.index[-180:], close[-180:], label='actual')
plt.plot(df.index[-180:], y_pred, label='predicted')
plt.legend()
plt.show()
future_dates = pd.date_range(start=df["日期"].iloc[-1], periods=180, freq='D')

future_df = pd.DataFrame({"日期": future_dates})


indicators_df = calculate_technical_indicators(future_df,df)




# 计算技术指标# 去除空缺值行
indicators_df.dropna(inplace=True)


print(indicators_df)

# 创建特征矩阵和标签向量
X_future = indicators_df.drop(columns=["日期"]).values

y_future = indicators_df["MA5"].values




model = LinearRegression()

model.fit(X[:-1], close[-142:])


future_predictions = model.predict(X_future)




# 使用历史数据训练线性回归模型并进行预测# 绘制预测结果图


plt.plot( future_predictions, label="Predicted Prices")


plt.xlabel("日期")

plt.ylabel("Stock Price")

plt.title("Stock Price Prediction for the Next 180 Days")

plt.legend()


plt.show()

