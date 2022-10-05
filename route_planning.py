import json
import pandas as pd

df = pd.read_csv('cleaned_with_xy.csv').loc[1]

#jdf = df.to_json('xy.json')


other_loc = {'name':['北京大学人民医院白塔寺院区','什刹海街道'], 'loc':['116.366224,39.924753','116.380275,39.93399'], 'note':['出生地','工作地']}
odf = pd.DataFrame(other_loc)
odf