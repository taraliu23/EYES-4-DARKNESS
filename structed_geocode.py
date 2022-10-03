import pandas as pd

# 删除没有坐标的题目 + 添加缺失值
df = pd.read_csv('raw.csv')
df.set_index('location_name', inplace=True)
df.drop(['人儿','油画','剪贴','彩墨','邮','缘','东陵','怀仁堂','献花','西市'], axis=0, inplace=True)
df.drop(labels='Unnamed: 0', axis=1, inplace=True)
df.at['故宫','geocodes_location']='116.397026,39.918058' #故宫博物院
df.at['象来街','geocodes_location']='116.365138,39.899030' #象来街招待所
# df.to_csv('cleaned.csv')

# 分开经纬度放入独立行
l = df['geocodes_location'].values.tolist()

# - 测试
coords = '116.350808,39.906608'
x = coords.split(",")
print(x[1])

# - 循环
x_list = []
y_list = []
for i in l:
    x = i.split(',')[0]
    y = i.split(',')[1]
    x_list.append(x)
    y_list.append(y)

df['x'] = x_list
df['y'] = y_list
df.to_csv('cleaned_with_xy.csv')