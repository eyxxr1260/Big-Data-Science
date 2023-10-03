import pandas as pd
import pylab
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('covid19.csv',encoding='big5')
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False


data["日期"] = pd.to_datetime(data["日期"])
data.set_index("日期", inplace=True)
start_date = pd.to_datetime('2022/4/1')
end_date = pd.to_datetime('2023/3/1')

sns.set(style="whitegrid")
plt.figure(figsize=(13, 9))
sns.lineplot(data=data.sum(axis=1))#每日確診人數的總數量
plt.xlabel('DATE')
plt.ylabel(' ')
# 設定 x 軸刻度間距和格式
#startdate = pd.to_datetime('2022-01-01')
#enddate = pd.to_datetime('2023-03-01')
#month_locator = mdates.MonthLocator()
#month_formatter = mdates.DateFormatter('%Y-%m-%d')
#plt.gca().xaxis.set_major_locator(month_locator)
#plt.gca().xaxis.set_major_formatter(month_formatter)

# 固定刻度為指定日期
fixed_dates = [
    '2020-01-22', '2020-07-03', '2021-01-01', '2021-06-26', '2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01', '2023-01-01', '2023-02-01', '2023-03-01' 
]
plt.xticks(fixed_dates, rotation=45)

plt.tight_layout()
plt.savefig('1a.png')
plt.show()



start_to_end_data = data.loc[start_date:end_date]
sns.set(style="whitegrid")
plt.figure(figsize=(13, 9))
sns.lineplot(data=start_to_end_data.sum(axis=1))#限定日期範圍內確診人數的總數量
plt.xlabel('DATE')
plt.ylabel(' ')
ax22 = plt.gca()
ax22.xaxis.set_major_locator(mdates.MonthLocator())
ax22.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('1b.png')
plt.show()



maxNumOfCases = data.loc[data.sum(axis=1).idxmax()][0:]#最多確診人數的日期
percentage = maxNumOfCases / data.sum(axis=1).max()
print(data.sum(axis=1).idxmax())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})
plt.figure(figsize=(10, 10))
plt.pie(percentage, autopct='%1.1f%%')
plt.title('2022-05-26確診分布')
plt.legend(percentage.index)
plt.axis('equal') 
plt.savefig('2a.png')
plt.show()


cityarea = {
    '縣市': ['臺北市', '新北市', '基隆市', '宜蘭縣', '桃園市', '新竹市', '新竹縣', '苗栗縣', '台中市', '彰化縣', '南投縣', '雲林縣', '嘉義市', '嘉義縣', '台南市', '高雄市', '屏東縣', '花蓮縣', '台東縣', '澎湖縣', '連江縣', '金門縣'],
    '面積': [2717997, 20525667, 1327589, 21436251, 12209540, 1041526, 14275369, 18203149, 22148968, 10743960, 41064360, 12908326, 600256, 19036367, 21916531, 29518524, 27756003, 46285714, 35152526, 1268641, 288000, 1516560]
}

x = cityarea['縣市']
people = data.loc[data.sum(axis=1).idxmax()][0:-1]
areas = cityarea['面積']
fig, ax = plt.subplots(figsize=(20, 10))

lns1 = ax.plot(x, people, "r-o", label="人數")
ax.plot(x, people, "r-o")
ax.set_ylabel("確診人數",size=20)
ax.set_xlabel("縣市",size=20)
ax2 = ax.twinx()
lns2 = ax2.plot(x, areas, "g--", label="面積")
ax2.plot(x, areas, "g--")
ax2.set_ylabel("縣市面積",size=20)
plt.xticks(range(len(x)), x, rotation=90)
lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc="best")
plt.title("縣市確診人數vs.縣市面積(2022-05-26)",size=20)
plt.savefig('2b.png')
plt.show()

fig_2c, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
ax1.imshow(plt.imread('2a.png'))
ax1.axis('off')
ax2.imshow(plt.imread('2b.png'))
ax2.axis('off')
fig_2c.savefig('2c.png')
plt.show()


