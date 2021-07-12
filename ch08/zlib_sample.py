import zlib


data = "Life is too short, You need python." * 10000
compress_data = zlib.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 1077 출력

org_data = zlib.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력
