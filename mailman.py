import xlwt
import re
import os

workbook = xlwt.Workbook()

command = 'sudo list_lists -b > listNames.txt'
os.system(command)

f = open("listNames.txt")
arrayListas = f.read().split("\n")

length = len(arrayListas)-1
row = 0
column = 0

for i in range(length):
    os.system('sudo list_members '+ arrayListas[i] + ' > ' +  arrayListas[i] + '.txt')

for x in range(length):
    t = open(arrayListas[x] + ".txt")
    listas = t.read().split("\n")
    sheet = workbook.add_sheet(arrayListas[x])
    lengthy = len(listas)
    row = 0
    for i in range(lengthy):
        sheet.write(row,column,listas[i])
        row += 1
    t.close()

workbook.save("prueba.xls")

f.close()