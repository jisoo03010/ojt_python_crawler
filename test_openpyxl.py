import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.append(['상품명', '가격', '구매 url'])
ws.append(['상품명', '가격', '구매 url'])
ws.append(['상품명', '가격', '구매 url'])
ws.append(['상품명', '가격', '구매 url'])
ws.append(['상품명', '가격', '구매 url'])
ws.append(['상품명', '가격', '구매 url'])

ws['A1'] = "Hello World"

wb.save("test1.xlsx")