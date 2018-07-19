# encoding : utf-8
import xlrd
import xlwt

def read_excel():
    data2 = xlrd.open_workbook(r'C:\Users\k\Desktop\python\2.xlsx')
    data3 = xlrd.open_workbook(r'C:\Users\k\Desktop\python\3.xlsx')
    sheet2 = data2.sheets()[0]
    sheet3 = data3.sheets()[0]
    print(sheet2.cell(1,2).value) #2行3列的数据