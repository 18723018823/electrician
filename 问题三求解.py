import pandas as pd # 读取CSV文件并创建DataFrame对象
df = pd.read_csv('wenjian_1.csv')
print(df)
print(df['predicted_mean'][0:10])
print(df['predicted_mean'][10:20])
print(df['predicted_mean'][20:30])
print(df['predicted_mean'][30:40])
print(df['predicted_mean'][40:50])
print(df['predicted_mean'][50:60])
c1=10000//2.98
print(sum(df['predicted_mean'][0:10]))
gu1=c1*sum(df['predicted_mean'][0:10])

c2=c1+10000//(sum(df['predicted_mean'][0:10])+2.98)
print(sum(df['predicted_mean'][10:20]))
gu2=c2*sum(df['predicted_mean'][10:20])

c3=c2+10000//(sum(df['predicted_mean'][0:10])+2.98+sum(df['predicted_mean'][10:20]))
gu3=c3*sum(df['predicted_mean'][20:30])

c4=c3+10000//(sum(df['predicted_mean'][0:10])+2.98+sum(df['predicted_mean'][10:20])+sum(df['predicted_mean'][20:30]))
gu4=c4*sum(df['predicted_mean'][30:40])

c5=c4+10000//(sum(df['predicted_mean'][0:10])+2.98+sum(df['predicted_mean'][10:20])+sum(df['predicted_mean'][20:30])+sum(df['predicted_mean'][30:40]))
gu5=c5*sum(df['predicted_mean'][40:50])

c6=c5+10000//(sum(df['predicted_mean'][0:10])+2.98+sum(df['predicted_mean'][10:20])+sum(df['predicted_mean'][20:30])+sum(df['predicted_mean'][30:40])+sum(df['predicted_mean'][40:50]))
gu6=c6*sum(df['predicted_mean'][50:60])

sum=gu1+gu2+gu3+gu4+gu5+gu6
print(sum)