
import re
import pandas as pd
import requests
import json
import numpy as np

# 提取OCR导出文件中的地名
with open('loc_name_from_ocr.txt', 'r') as file:
    loc_name = file.read().replace('\n', '')
    file.close()
pattern=re.compile("[\u4e00-\u9fa5]+")
loc_list = pattern.findall(loc_name)

# 将地名和地理编码变为结构化文本
df = pd.DataFrame(loc_list, columns=['location_name'])
df.index = np.arange(1, len(df) + 1)

# 高德地图web API正地理编码查询
key = '0b8fa63575fef96b50e752c13241852b'
base = 'https://restapi.amap.com/v3/geocode/geo'

#parameters = {'address': '后海', 'key': key, 'city':'北京'}
#test = requests.get(base, parameters)
#json_test = json.loads(test.text)
#loc_test = json_test['geocodes'][0]['location']
#print(loc_test)

location_list = []

for i in loc_list:
    para = {'address': i, 'key': key, 'city':'北京'}
    try:
        reqs = requests.get(base, para)
        json_info = json.loads(reqs.text)
        loc = json_info['geocodes'][0]['location']
        location_list.append(loc)
    except:
        location_list.append('null')

df['geocodes_location']= location_list
df.to_csv('raw.csv')

df.set_index('location_name')

