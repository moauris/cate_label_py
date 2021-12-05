import datetime as dt
import xlwings as xw
import pandas as pd
import numpy as np
import StockDataLoader as loader
import StockDataLabeler as labeler
import StockDataWriter as writer

# 读取一个工作簿
# 判断一个工作表是否符合同步规则
# 同步时，标记板块分类
# 输出结果
inputdir = input("请输入工作表绝对路径：")
#data = loader.ReadData(inputdir, "股票")
#data = loader.ReadData(inputdir, "偏股混合")
data = loader.ReadData(inputdir, "灵活混合")
processedData = labeler.LabelDFrame(data)
writer.WriteData(processedData, "output.xlsx")
input("任意键结束程序")