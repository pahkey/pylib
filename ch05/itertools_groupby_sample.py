import itertools
import operator
import pprint

data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]

data = sorted(data, key=operator.itemgetter('blood'))  # groupby 전 분류기준으로 소트를 해야 한다.
grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))

result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)  # group_data는 이터레이터이므로 리스트로 바꾼다.

pprint.pprint(result)
