from openpyxl import Workbook

# 새로운 엑셀 파일 생성을 위한 클래스 변수 생성
xlsx = Workbook()

# '새로운시트2' 이름을 가진 시트 생성
sheet = xlsx.create_sheet('새로운시트2')
sheet['A1'] = '데이터'

# 엑셀 파일로 저장
xlsx.save('other.xlsx')

