# 热力图模块说明
## 思路
1. 将武汉街道数据处理为xx.csv
   + overall.csv
   + originalorder.csv 
   + **2020-01-01.csv**
2. 仿照平台的heatmap.json文件处理csv文件
   + 2020-01-01.csv
   + **2020-01-01.json**
3. 遍历文件名，叠加图层
   + 2020-xx-xx.json
   + **heatmap**
## 数据wuhandata
1. format.latlon
   平台json文件模板，其中经纬度已更新为wuhan-street
2. format.originalorder
   “经纬度-mag”格式文件，其中经纬度与latlon顺序一致
3. original
   原始数据，其中overall.csv为qgis处理的总数据
4. daily_csv
5. daily_json
## 源文件
1. wh_heatmap.html
   + 显示heatmap
   + arr需手动更新
2. daily.py
   + 将csv处理为json
   + 读取和写入的2020-xx-xx.json文件需手动更新
3. directory.py
   + 生成全部文件的字符串列表
   + 将list复制到html文件的arr
4. time.html
   + 测试setTimeout()和for循环搭配使用
5. demo.html
   + 测试 单个heatmap.json文件读取是否正常