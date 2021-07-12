import nntplib
import email

s = nntplib.NNTP('news.gmane.io')
resp, count, first, last, name = s.group('gmane.comp.python.devel')
resp, overviews = s.over((last - 2, last))


def get_plain_body(message):
    if message.is_multipart():
        for part in message.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)
                break
    else:
        body = message.get_payload(decode=True)
    return body.decode('utf-8')


for _id, over in overviews:
    print('제목:', nntplib.decode_header(over['subject']))
    print('작성자:', nntplib.decode_header(over['from']))
    print('작성일시:', nntplib.decode_header(over['date']))
    resp, info = s.article(_id)
    message = email.message_from_bytes(b'\n'.join(info.lines))
    body = get_plain_body(message)
    print('\n', body)
