from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

SMTP_SERVER = "smtp.naver.com"
SMTP_PORT = 465
SMTP_USER = "jabez1021@naver.com"
# real password #
SMTP_PASSWORD = "8MRCFMECM64Q"

def send_mail(name, recvs, cc, hidden_cc, ontents, attachment=False):
    msg = MIMEMultipart("alternative")

    if attachment:
        msg = MIMEMultipart('mixed')

    msg['From'] = SMTP_USER
    msg['To'] = recvs
    msg['CC'] = ccmsg['Subject'] = name+'님, 메일이 도착했습니다.'

    text = MIMEText(contents)
    msg.attach(text)

    