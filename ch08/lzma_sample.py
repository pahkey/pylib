import lzma

data = "Life is too short, You need python." * 10000
compress_data = lzma.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 220 출력

org_data = lzma.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력

assert data == org_data
