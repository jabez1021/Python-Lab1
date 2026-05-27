from openpyxl import Workbook

# 새로운 엑셀 파일 생성을 위한 클래스 변수 생성
xlsx = Workbook()
sheet = xlsx.active

# 첫번째 행에 데이터 추가
sheet.append(['A1-data', 'B1-data', 'C1-data'])
# 두번째 행에 데이터 추가
sheet.append(['A2-data', 'B2-data', 'C2-data'])

# 엑셀 파일로 저장
xlsx.save('other.xlsx')



