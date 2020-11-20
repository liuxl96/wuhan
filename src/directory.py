#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np

filePath = './wuhandata/daily_json'  #遍历文件
dir_list = os.listdir(filePath)
dir_num = np.shape(dir_list)

print(dir_list)
print(dir_num)