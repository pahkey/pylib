#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()

a = form.getvalue('a')
b = form.getvalue('b')

result = int(a) * int(b)

print('Content-type: text/plain')
print()
print(f'Result:{result}')
