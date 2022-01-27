import pandas as pd

def add_avg():

    dict1 = {}
    df = pd.read_excel('Info.xlsx')

    for i, j in zip(df, df.dtypes):
        if j in ['float64', 'int64'] and i != 'E_id':
            dict1[i] = df[i].mean()



    df = df.append(dict1, ignore_index=True)
    print(df)

add_avg()