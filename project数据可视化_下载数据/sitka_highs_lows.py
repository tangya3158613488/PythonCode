import csv
from datetime import datetime

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期、最高温度和最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(lows)

    # 根据最高温度和最低温度绘制图形
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')

    # 设置图形格式
    ax.set_title("2018年每日最高温度", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("温度（F）", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
