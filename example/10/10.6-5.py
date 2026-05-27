import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name('alghost-auto-...json', scope)
gs = gspread.authorize(credentials)
doc = gs.create('새로운 문서')
# 첫번째 시트 가져오기
ws = doc.get_worksheet(0)
# A1셀에 데이터를 씀
ws.update_acell('A1', '데이터입니다')
