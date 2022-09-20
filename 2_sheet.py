from openpyxl import Workbook

wb = Workbook()
# wb.active
ws = wb.create_sheet() #새로운 sheet 기본 이름으로 생성

ws.title = "Mysheet"  # 시트 이름 변경
ws.sheet_properties.tabColor ="ff66ff" # RGB 형태로 입력

wb.save("sample.xlsx")



