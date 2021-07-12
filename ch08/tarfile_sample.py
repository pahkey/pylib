import tarfile

# 여러파일 합치기
with tarfile.open('mytext.tar', 'w') as mytar:
    mytar.add('a.txt')
    mytar.add('b.txt')
    mytar.add('c.txt')

# 여러파일 해제하기
with tarfile.open('mytext.tar') as mytar:
    mytar.extractall()
