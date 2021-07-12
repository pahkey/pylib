import pdb

numbers = [1, 2, 3]
for i in range(len(numbers)):
    pdb.set_trace()  # 중단점 설정
    if numbers[i] % 2 == 0:
        del numbers[i]

print(numbers)
