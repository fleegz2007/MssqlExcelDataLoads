import openpyxl
import config
from openpyxl import load_workbook

def extracthdct():
    datalist = []
    wb = load_workbook(config.landingzone + config.filename, data_only=True)
    ws = wb.active
    minrow = ws.min_row
    maxrow = ws.max_row
    mincol = ws.min_column
    maxcol = ws.max_column
    print(maxcol)
    print("Beginning extraction from Excel document...")
    for i in range (mincol, maxcol+1):
        datalist.append([])
        for j in range (minrow+1, maxrow):
            #Unmute and use this if you want to set conditions of dataload if ws.cell(row=j, column=i).value == 'condition1' or ws.cell(row=j, column=i).value == 'condition2' or ws.cell(row=j, column=i).value == 'condition3':
                datalist[i-1].append(ws.cell(row=j, column=i).value)
    return datalist