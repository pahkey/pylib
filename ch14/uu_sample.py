import uu

# 이미지를 텍스트로 변환
uu.encode('test.jpg', 'result.txt')

# 텍스트를 다시 이미지로 변환
uu.decode('result.txt', 'test1.jpg')
