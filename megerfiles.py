import os
import re
from pandas import DataFrame
import pandas as pd

def enum_files(dir):
    files = [name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]
    return files

def meger_fies(dir, files):
    data = None
    for file in files:
        xlsx = pd.ExcelFile(os.path.join(dir, file))
        df = pd.read_excel(xlsx, 'Sheet1')
        data = pd.concat([data, df])

def get_date_from_file_name(file):
    re.split(r'[_.]', files[0])