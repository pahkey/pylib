def leap_year(year):
    """ year가 윤년이면 True 아니면 False를 리턴한다

    >>> leap_year(1)
    False
    >>> leap_year(4)
    True
    >>> leap_year(1200)
    True
    >>> leap_year(700)
    False
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
