import hashlib
import os


def check_passwd():
    if os.path.exists('passwd.txt'):
        before_passwd = input('기존 비밀번호를 입력하세요:')
        m = hashlib.sha256()
        m.update(before_passwd.encode('utf-8'))
        with open('passwd.txt', 'r') as f:
            return m.hexdigest() == f.read()
    else:
        return True


if check_passwd():
    passwd = input('새로운 비밀번호를 입력하세요:')
    with open('passwd.txt', 'w') as f:
        m = hashlib.sha256()
        m.update(passwd.encode('utf-8'))
        f.write(m.hexdigest())
else:
    print("비밀번호가 일치하지 않습니다.")
