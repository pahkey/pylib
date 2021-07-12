import telnetlib

# 관리하는 서버리스트 (호스트, 아이디, 비밀번호)
SERVER = [
    ('10.12.50.111', 'foo', 'foo1234'),
    ('10.12.50.112', 'bar', 'bar1234'),
    # ... 생략 ...
]

for host, user, password in SERVER:
    tn = telnetlib.Telnet(host)
    tn.read_until(b"login: ")
    tn.write(user.encode('utf-8') + b'\n')

    tn.read_until(b"Password: ")
    tn.write(password.encode('utf-8') + b'\n')

    tn.write(b'free\n')
    tn.write(b'exit\n')

    with open(host+'_result.txt', 'w') as f:
        f.write(tn.read_all().decode('utf-8'))
