import pandas

def solution():
    df = pandas.read_csv("day1.csv")
    print(df.nunique())
    return df.holiday.unique()
print(solution())