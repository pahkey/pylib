import time
import atexit


def handle_exit():
    print("프로그램 종료시 반드시 호출되어야 합니다.")


atexit.register(handle_exit)  # handle_exit 함수가 프로그램 종료시 호출되도록 등록한다.
while True:
    print("작업중..")
    time.sleep(1)
