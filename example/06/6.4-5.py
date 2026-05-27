from openpyxl import load_workbook

# result.xlsx를 읽은 후 기본 시트를 선택
xlsx = load_workbook('result.xlsx')
sheet = xlsx.active

# A~B 열을 가져옴
cols = sheet['A:B']
# 각 열을 가져오기 위한 반복문
for col in cols:
    # 각 열의 셀을 가져오기 위한 반복문
    for cell in col:
        print(cell.value)


