import hmac
import hashlib

SECRET_KEY = 'PYTHON'

with open('message_digest.txt') as f:
    message_digest = f.read()

with open('message.txt') as f:
    message = f.read()
    m = hmac.new(SECRET_KEY.encode('utf-8'), message.encode('utf-8'),
                 hashlib.sha256)

    if m.hexdigest() == message_digest:
        print("메시지가 변조되지 않았습니다. 안전합니다.")
