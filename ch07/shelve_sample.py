import shelve


def save(key, value):
    with shelve.open('shelve.dat') as d:
        d[key] = value


def get(key):
    with shelve.open('shelve.dat') as d:
        return d[key]


save('number', [1, 2, 3, 4, 5])
print(get('number'))  # [1, 2, 3, ,4, 5] 출력
