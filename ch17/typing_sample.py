from typing import List


def sum_list(numbers: List[int]) -> int:
    return sum(n for n in numbers)


result = sum_list([1, 2, '3', 4])
print(result)
