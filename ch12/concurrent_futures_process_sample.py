import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)
    return result  # 결과를 리턴하도록 변경


if __name__ == '__main__':
    import concurrent.futures

    start = time.time()

    total_result = 0
    pool = concurrent.futures.ProcessPoolExecutor(max_workers=4)

    procs = []
    for i in range(4):
        procs.append(pool.submit(heavy_work, i))

    for p in concurrent.futures.as_completed(procs):
        total_result += p.result()

    end = time.time()

    print("수행시간: %f 초" % (end - start))
    print("총결괏값: %s" % total_result)
