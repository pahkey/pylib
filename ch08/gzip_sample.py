import gzip

data = "Life is too short, you need python." * 10000

with gzip.open('data.txt.gz', 'wb') as f:
    f.write(data.encode('utf-8'))

# 저장된 파일을 확인해 보았더니 파일사이즈가 1097 바이트로 표시된다.

with gzip.open('data.txt.gz', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data
