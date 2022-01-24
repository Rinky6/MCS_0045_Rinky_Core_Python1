import pandas as pd
import xml.etree.ElementTree as et


def solution():
    xml_data = open('data1.xml', 'r').read()  # Read file
    root = et.XML(xml_data)  # Parse XML

    data = []
    cols = []

    for i, child in enumerate(root):
    # print(i,child)
        data.append([subchild.text for subchild in child])
        cols.append(child.tag)

    df = pd.DataFrame(data).T  # Write in DF and transpose it
    df.columns = cols  # Update column names
    print(df)
    rst=list(df["Marks"])
    print(rst)
    rst1 = 0
    for i in rst:
        rst1 = rst1+int(i)
    print(rst1)
    return rst1 / len(rst)

rst = solution()
print("average of marks : " , rst)