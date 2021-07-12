import functools
import time


def elapsed(original_func):
    @functools.wraps(original_func)  # 여기에 추가!!
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result

    return wrapper


@elapsed
def add(a, b):
    """ 두 수 a, b를 더한값을 리턴하는 함수 """
    return a + b


print(add)  # 함수명 출력
help(add)  # 함수의 독스트링 출력
