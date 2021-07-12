from graphlib import TopologicalSorter

ts = TopologicalSorter()

# 규칙1
ts.add('영어중급', '영어초급')  # 영어중급의 선수과목은 영어초급
ts.add('영어고급', '영어중급')  # 영어고급의 선수과목은 영어중급

# 규칙2
ts.add('영어문법', '영어중급')  # 영어문법의 선수과목은 영어중급
ts.add('영어고급', '영어문법')  # 영어고급의 선수과목은 영어문법

# 규칙3
ts.add('영어회화', '영어문법')  # 영어회화의 선수과목은 영어문법

print(list(ts.static_order()))  # 위상정렬한 결과를 출력
