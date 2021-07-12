import imaplib
import email
from email.header import decode_header, make_header

server = imaplib.IMAP4_SSL('imap.gmail.com')
server.login('your_gmail_id', 'your_gmail_passwd')

rv, data = server.select()
recent_no = data[0]

rv, fetched = server.fetch(recent_no, '(RFC822)')
message = email.message_from_bytes(fetched[0][1])

fr = make_header(decode_header(message.get('From')))
subject = make_header(decode_header(message.get('Subject')))

if message.is_multipart():
    for part in message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)
            break
else:
    body = message.get_payload(decode=True)

body = body.decode('utf-8')

print(f"보낸사람:{fr}")
print(f"제목:{subject}")
print(f"내용:{body}")

server.close()
server.logout()
