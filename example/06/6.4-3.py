from openpyxl import load_workbook

# result.xlsx를 읽은 후 기본 시트를 선택
xlsx = load_workbook('result.xlsx')
sheet = xlsx.active

# 첫번째 열을 가져옴
col = sheet['A']
# 첫번째 열의 각 행 값을 출력
for cell in col:
    print(cell.value)


