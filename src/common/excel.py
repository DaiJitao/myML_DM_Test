# encoding : utf-8
import xlrd
import xlwt

def read_excel():
    data2 = xlrd.open_workbook(r'C:\Users\k\Desktop\python\2.xlsx')
    data3 = xlrd.open_workbook(r'C:\Users\k\Desktop\python\3.xlsx')
    sheet2 = data2.sheets()[0]
    sheet3 = data3.sheets()[0]
    print(sheet2.cell(1,2).value) #2行3列的数据

def read_excel(path, cell_line , cell_col, sheetIndex = 0):
    data = xlrd.open_workbook(path)
    sheet = data.sheets()[sheetIndex]
    print(sheet.cell(cell_line, cell_col).value) #2行3列的数据

def make_excel():
    data2 = xlrd.open_workbook(r'C:\Users\k\Desktop\python\2.xlsx')
    data3 = xlrd.open_workbook(r'C:\Users\k\Desktop\python\3.xlsx')
    sheet2 = data2.sheets()[0]
    sheet3 = data3.sheets()[0]
    print(sheet2.cell(1,2).value)
    build_excel(sheet2.cell(1,2).value)

def build_excel(value, savedPath, line_index=0, col_index=0, sheetName='1', ):
    data4 = xlwt.Workbook()
    sheet4 = data4.add_sheet(sheetname=sheetName)
    sheet4.write( line_index, col_index, value)
    data4.save(savedPath)


make_excel()