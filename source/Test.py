import datetime as dt
import xlwings as xw
import pandas as pd
import numpy as np
import StockDataRow as sdr

# 读取一个工作簿
# 判断一个工作表是否符合同步规则
# 同步时，标记板块分类
# 输出结果
inputdir = input("请输入工作表绝对路径：")

book = xw.Book(inputdir)
sheets = book.sheets

sheet = sheets[0]

if(sheet.range("BAX3").value == None):
    print("Is Correct")

print(sdr.CategoryLabeler.Judge("公用事业"))

input("任意键结束程序")