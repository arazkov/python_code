import openpyxl


wb = openpyxl.load_workbook(filename = '08_2020.xlsx')
sheet = wb['а']

#считываем значение определенной ячейки
val = sheet['A2'].value
print(val)
#считываем заданный диапазон
#vals = [v[0].value for v in sheet.range('A1:A2')]
a = 0
for i in range(70,75):
    sheet[f'{chr(i+1)}26'] = f'8 {20+a if a < 4 else "00"}'
    a +=1
wb.save('08_2020.xlsx')
