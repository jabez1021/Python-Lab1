from openpyxl import load_workbook

# result.xlsx를 읽은 후 기본 시트를 선택
xlsx = load_workbook('result.xlsx', read_only=True)
sheet = xlsx.active

# 첫번째 행을 가져옴
row = sheet['1']
# 첫번째 행의 각 컬럼의 값을 출력
for cell in row:
    print(cell.value)


