import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
#df = pd.read_excel('data.xlsx' ,index_col= 0 , header= 0)
def solution():
    df = pd.read_excel('data.xlsx' )
    print(df)
    rst=list(df['Marks'])

    return sum(rst) / len(rst)
avg = solution()
print("Average of marks : ", avg)
