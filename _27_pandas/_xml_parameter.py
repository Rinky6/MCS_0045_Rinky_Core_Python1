import pandas as pd
import xml.etree.ElementTree as et


def solution():
    xml_data = open('data1.xml', 'r').read()
    root = et.XML(xml_data)
    data = []
    cols = []
    for i, child in enumerate(root):
        cols.append(child.tag)

    df = pd.DataFrame(data).T
    print(cols)
rst = solution()
print("")