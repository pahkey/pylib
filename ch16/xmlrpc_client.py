import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.system.listMethods())  # 사용 가능한 함수들을 출력한다.

result = s.wikidocs(2)
print(result)  # http://wikidocs.net/2 의 컨텐츠를 출력한다.
