def a():
    result = []
    for i in range(10000):
        result.append(i)
    return result


def b():
    return [i for i in range(10000)]


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("a()", number=100, globals=globals()))
    print(timeit.timeit("b()", number=100, globals=globals()))
