import os
import xlwings as xw
import pandas as pd

def enum_files(path):
    excel_files = []
    for root, dirs, names in os.walk(path):
        for name in names:
            excel_files.append(os.path.join(root, name))
    return excel_files

def merge_excel_file(path):
    merge_data = []
    excel_files = enum_files(path)
    app = xw.App(visible = False)
    for excel_file in excel_files:
        wb = app.books.open(excel_file)
        rng = wb.sheets[0].range('a1').options(expand = 'table').value
        merge_data.extend(rng)
        wb.close()
    wb_merge_excle = xw.App(visible = False).books.add()
    wb_merge_excle.sheets[0].range('a1').value = merge_data
    merge_excel_file_path = os.path.join(path, 'merge.xlsx')
    wb_merge_excle.save(merge_excel_file_path)
    wb_merge_excle.close()