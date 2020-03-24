import xlwt
import re

workbook = xlwt.Workbook()

sheet = workbook.add_sheet('Primera hoja')
sheet1 = workbook.add_sheet('Segunda hoja')

sheet.write_string(0,0,'Prueba')
sheet1.write_string(0,2,'Prueba1')

workbook.save('prueba.csv')