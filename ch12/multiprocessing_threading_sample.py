import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import threading

    start = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=heavy_work, args=(i, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # 스레드가 모두 종료될 때까지 기다린다.

    end = time.time()

    print("수행시간: %f 초" % (end - start))
