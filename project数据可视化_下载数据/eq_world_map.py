import plotly.express as px
import pandas as pd

from project数据可视化_下载数据.eq_explore_data import lons, lats, titles, mags

filename = 'data/eq_data_30_day_m1.json'
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
data.head()
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)
fig.write_html('global_earthquake.html')
fig.show()