from openpyxl import load_workbook

# 기존 엑셀 파일을 위한 클래스 변수 생성
xlsx = load_workbook('other.xlsx')

# '새로운시트2' 시트를 가져옴
sheet = xlsx['새로운시트2']

# 내용 출력
print(sheet['A1'].value)

