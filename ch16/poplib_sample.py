import poplib
import email
from email.header import decode_header, make_header

server = poplib.POP3_SSL('pop.googlemail.com')
server.user('your_gmail_id')
server.pass_('your_gmail_passwd')

recent_no = server.stat()[0]
raw_email = b'\n'.join(server.retr(recent_no)[1])
message = email.message_from_bytes(raw_email)

fr = make_header(decode_header(message.get('From')))
subject = make_header(decode_header(message.get('Subject')))

if message.is_multipart():
    for part in message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
else:
    body = message.get_payload(decode=True)

body = body.decode('utf-8')

print(f"보낸사람:{fr}")
print(f"제목:{subject}")
print(f"내용:{body}")
