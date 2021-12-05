# 从Pandas DataFrame 对象写入到新的工作簿
import pandas as pd
import xlwings as xw

def WriteData(data: pd.DataFrame, NewName : str):
    book = xw.Book()
    sheet = book.sheets[0]
    sheet["A1"].value = data
    
    book.save(NewName)