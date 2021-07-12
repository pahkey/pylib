import hmac
import hashlib

SECRET_KEY = 'PYTHON'

important_message = '이것은 누구나 볼 수 있는 원본 파일의 내용이다.'

with open('message.txt', 'w') as f:
    f.write(important_message)

with open('message_digest.txt', 'w') as f:
    m = hmac.new(SECRET_KEY.encode('utf-8'), important_message.encode('utf-8'),
                 hashlib.sha256)
    f.write(m.hexdigest())
