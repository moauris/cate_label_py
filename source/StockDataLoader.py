# 从某个 xlsx 中读取数据为 Pandas DataFrame 对象
import pandas as pd
import xlwings as xw

def ReadData(path: str, sheetName: str) -> pd.DataFrame:
    book = xw.Book(path)
    sheet = book.sheets[sheetName]

    return sheet["A1"].expand().options(pd.DataFrame).value