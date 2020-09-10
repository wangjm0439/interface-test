#!/usr/bin/env python
# encoding: utf-8
import xlrd
from util.oper_interfacedb import Oper_sql
import os

def read_excel():
    try:
        #workbooks =os.getcwd()
        #print(workbooks)
        workbook=xlrd.open_workbook(filename=r"D:\work_space\python_space\interface-test\interface-test\run\uploads\interfacedata.xlsx")
    except:
        workbook = xlrd.open_workbook(filename=r"D:\work_space\python_space\interface-test\interface-test\run\uploads\interfacedata.xls")
    table=workbook.sheet_by_index(0)
    #print(table)
    row=table.nrows
    #col=table.ncols
    #print(row,col)
    for i in range(1,row):
        row_value=table.row_values(i)
        print(row_value)
        insert_data=Oper_sql()   #intername,interaddr,header,param,option,author, descp, expected, account
        insert_data.insert_interfaceinfo(row_value[0],row_value[3],row_value[2],row_value[5],row_value[4],row_value[6],row_value[1],int(row_value[7]),row_value[8])

if __name__=="__main__":
    read_excel()
    #path1=os.getcwd()
    #print(path1 + "/run/uploads/interfacedata.xlsx")
    os.path.dirname(".")