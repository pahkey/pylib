import bisect

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect([60, 70, 80, 90], score)  # 점수가 정렬되어 삽입될 수 있는 포지션을 반환
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)
