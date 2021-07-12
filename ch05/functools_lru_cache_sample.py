import urllib.request
from functools import lru_cache


@lru_cache(maxsize=32)
def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'


first_6 = get_wikidocs(6)
first_7 = get_wikidocs(7)

second_6 = get_wikidocs(6)
second_7 = get_wikidocs(7)

assert first_6 == second_6  # 처음 요청한 6번 페이지의 내용과 두번째 요청한 6번 페이지의 내용이 같은지를 확인
assert first_7 == second_7
