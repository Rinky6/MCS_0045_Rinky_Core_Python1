import pandas as pd

def func():

    df = pd.read_excel('Info.xlsx')
    for i, j in zip(df, df.dtypes):
        if j in ['float64', 'int64'] and i!='E_id':
            print(i, df[i].mean())

func()