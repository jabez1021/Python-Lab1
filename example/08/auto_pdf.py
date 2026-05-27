import re
from openpyxl import Workbook
from pdfminer.high_level import extract_text

wb = Workbook()
ws = wb.active
ws.append([
    '계약금액', '갑_주소', '갑_회사명', '갑_대표자', '갑_연락처',
    '을_주소', '을_회사명', '을_대표자', '을_연락처'
])

files = ['sample1.pdf', 'sample2.pdf', 'sample3.pdf']
for pdf in files:
    text = extract_text(pdf)
    lines = text.split('\n')

    row = []
    for line in lines:
        if '일금' in line and '부가세포함' in line:
            price = ''.join(re.findall(r'\d+', line))
            row.append(price)

        if len(row) < 5:
            if '주        소:' in line:
                a_address = line.replace('주        소:', '').strip()
                row.append(a_address)

            if '회  사  명:' in line:
                a_company = line.replace('회  사  명:', '').strip()
                row.append(a_company)

            if '대  표  자:' in line:
                a_boss = line.replace('대  표  자:', '').replace('(인)', '').strip()
                row.append(a_boss)

            if '연  락  처:' in line:
                a_contact = line.replace('연  락  처:', '').strip()
                row.append(a_contact)
        else:
            if '주        소:' in line:
                b_address = line.replace('주        소:', '').strip()
                row.append(b_address)

            if '회  사  명:' in line:
                b_company = line.replace('회  사  명:', '').strip()
                row.append(b_company)

            if '대  표  자:' in line:
                b_boss = line.replace('대  표  자:', '').replace('(인)', '').strip()
                row.append(b_boss)

            if '연  락  처:' in line:
                b_contact = line.replace('연  락  처:', '').strip()
                row.append(b_contact)

    ws.append(row)
wb.save('result.xlsx')