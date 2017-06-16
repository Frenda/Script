import os
import re
from pandas import DataFrame
import pandas as pd
import numpy as np

def enum_files(dir):
    files = [name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]
    return files

def get_date_from_file_name(file):
    return re.split(r'[_.]', file)[:2]

def str_to_int(df):
    data = []
    pattern = re.compile(r'万')
    for i in df.点击:
        if i == '--':
            data.append(np.nan)
        elif i.find('万') != -1:
            data.append(int(float(pattern.sub('', i)) * 10000))
        else:
            data.append(int(i))
    return data

def meger_files(dir):
    data = None
    files = enum_files(dir)
    for file in files:
        xlsx = pd.ExcelFile(os.path.join(dir, file))
        df = pd.read_excel(xlsx, 'Sheet1')
        data = pd.concat([data, df])
        date = get_date_from_file_name(file)
        data['年'] = date[0]
        data['月'] = date[1]
    data = data.reset_index(drop = True)
    data.点击 = str_to_int(data)
    writer = pd.ExcelWriter(os.path.join(dir, 'output.xlsx'))
    data.to_excel(writer,'Sheet1')
    writer.save()

