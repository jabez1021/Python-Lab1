from openpyxl import Workbook

# 새로운 엑셀 파일 생성을 위한 클래스 변수 생성
xlsx = Workbook()
sheet = xlsx.active

# A1 셀에 문자열 값 추가
sheet['A1'] = 'my input data'

# 엑셀 파일로 저장
xlsx.save('other.xlsx')



