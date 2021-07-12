import urllib.request


def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'


if __name__ == '__main__':
    import time
    import concurrent.futures

    start = time.time()

    pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    threads = []
    for page in pages:
        threads.append(pool.submit(get_wikidocs, page))

    concurrent.futures.wait(threads)  # 스레드가 모두 종료되기를 기다린다.

    end = time.time()

    print("수행시간: %f 초" % (end - start))
