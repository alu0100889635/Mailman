import os
import re
import xlwt
import sys

workbook = xlwt.Workbook()

f = open("salida.txt")
arrayFichero = f.read().split("---------")
length = len(arrayFichero)-1
arrayNuevo = []

for i in range(length):
    arrayNuevo.append(arrayFichero[i].split("\n"))

leng = len(arrayNuevo)
column = 0
row = 0

sheet1 = workbook.add_sheet(arrayNuevo[0][0])
for y in range(1, len(arrayNuevo[0])-1):
    sheet1.write(row,column,arrayNuevo[0][y])
    row +=1

for x in range(1, leng):
    row = 0
    for y in range(len(arrayNuevo[x])-1):
        if y == 1:
            sheet = workbook.add_sheet(arrayNuevo[x][y])
            for z in range(2,len(arrayNuevo[x])-1):
                sheet.write(row,column,arrayNuevo[x][z])
                row += 1

workbook.save("Listas_correos.xls")
f.close()