#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 1. .json文件和.csv文件的经纬度顺序及数量需保持一致，分别包含py_data；csv_coord_list和csv_mag_list
# 2. csv包含经纬度及各个街道每天的确诊人数

import json
import pandas as pd
import numpy as np

def strTofloat(data):  #字符串列表转换为数字列表:['123','456']->[123,456]
    temp = []
    for i in range(0,2):  #适用每个data列表只有2项
        item = float(data[i])
        temp.append(item)
    return temp 

with open('./wuhandata/format/latlon.json','r') as f1:  #读取平台格式数据
    json_data = f1.read()
    py_data = json.loads(json_data)

csv_data = pd.read_csv('./wuhandata/daily_csv/2020-01-31.csv')  #读取每天的"经纬度:人数"数据

csv_nan_data = csv_data.fillna(0)
csv_coord_list = csv_nan_data['coord_coordinates'].values.tolist()  

for i in range(len(csv_coord_list)):    #json文件的经纬度string转为list
    item = csv_coord_list[i].split(",")
    csv_coord_list[i] = strTofloat(item)

csv_mag_list = csv_nan_data['mag'].values.tolist()  #json文件的mag字符串转为list，与json顺序对应

lat_items = py_data['features']    # lat_items-type:list, item-type:dict

for item in lat_items: #更新json文件的mag数据
    lat_lon = item['geometry']['coordinates']  
    for i in range(len(csv_coord_list)):  
        if lat_lon == csv_coord_list[i]:
            py_data['features'][i]['properties']['mag'] = csv_mag_list[i]

jsonstr = json.dumps(py_data, indent=2, separators=(',',":"))
with open('./wuhandata/daily_json/2020-01-31.json','w') as f2:
    f2.write(jsonstr)