import os
import xlwings as xw

def enum_files(path):
    excel_files = []
    for root, dirs, names in os.walk(path):
        for name in names:
            excel_files.append(os.path.join(root, name))
    return excel_files

def merge_excel_file(path):
    merge_data = []
    data_len = 0
    ##枚举指定目录下的excel文件
    excel_files = enum_files(path)
    is_first_open = False
    ##打开一个以不可见的App
    app = xw.App(visible = False)
    ##创建用来保存合并数据的工作簿
    wb_merge_excle = xw.App(visible = False).books.add()
    for excel_file in excel_files:
        ##打开excel文件
        wb = app.books.open(excel_file)
        if is_first_open == False:
            ##第一次读取数据
            rng = wb.sheets[0].range('a1').options(expand = 'table').value
            data_len = len(rng) + 1
            ##写入数据
            wb_merge_excle.sheets[0].range('a1').value = merge_data
            is_first_open = True
        else:
            ##忽略第一行数据
            rng = wb.sheets[0].range('a2').options(expand = 'table').value
            write_data_location = ''.join(['a', str(data_len)])
            wb_merge_excle.sheets[0].range(write_data_location).value = merge_data
            data_len = len(rng) + 1
        ##把数据保存起来
        merge_data.extend(rng)
        wb.close()
    merge_excel_file_path = os.path.join(path, 'merge.xlsx')
    wb_merge_excle.save(merge_excel_file_path)
    wb_merge_excle.close()