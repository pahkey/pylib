import bz2

data = "Life is too short, You need python." * 10000
compress_data = bz2.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 163 출력

org_data = bz2.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력

assert data == org_data
