from openpyxl import load_workbook

# result.xlsx를 읽은 후 기본 시트를 선택
xlsx = load_workbook('result.xlsx', read_only=True)
sheet = xlsx.active

# A1 셀의 데이터를 출력
print(sheet['A1'].value)
# B1 셀의 데이터를 출력
print(sheet['B1'].value)



