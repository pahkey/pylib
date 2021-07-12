import os
import smtplib
from email.encoders import encode_base64
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

msg = MIMEMultipart()

msg['From'] = 'pahkey@naver.com'
msg['To'] = 'pahkey@gmail.com'
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = Header(s='파일첨부 메일송신 테스트', charset='utf-8')
body = MIMEText('첨부된 파일 2개를 확인해 주세요.', _charset='utf-8')
msg.attach(body)

files = list()
files.append('c:/projects/pylib/test.pdf')
files.append('c:/projects/pylib/test.jpg')

for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f, "rb").read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)

mailServer = smtplib.SMTP_SSL('smtp.naver.com')
mailServer.login('pahkey@naver.com', 'xxxxxxxx')  # 본인의 계정과 비밀번호를 사용하자.
mailServer.send_message(msg)
mailServer.quit()
