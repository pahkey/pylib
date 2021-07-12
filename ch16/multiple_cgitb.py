#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()

print('Content-type: text/html')  # Content-type을 최상단에서 먼저 출력해 준다.
print()

form = cgi.FieldStorage()

a = form.getvalue('a')
b = form.getvalue('b')

result = int(a) * int(b)

print(f'Result:{result}')
