import xlwt
import re

workbook = xlwt.Workbook()

f = open("listNames.txt")
arrayListas = f.read().split("\n")

# comando para las listas y meterlo en fichero listNames.txt
# comando para los correos de cada lista y meterlo en ficheros List-X.txt
length = len(arrayListas)
row = 0
column = 0

for x in range(length):
    fichero = ".txt"
    t = open(arrayListas[x] + fichero)
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


#exreg= arrayListas[i]
#('*@*.*')
#expresioncorreo = '*@*.*'

""" sheet = workbook.add_sheet('Primera hoja')
sheet1 = workbook.add_sheet('Segunda hoja')

sheet.write(0,0,'Prueba')
sheet1.write(0,2,'Prueba1')

workbook.save('prueba.xls') """