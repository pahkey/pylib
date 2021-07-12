from functools import partial


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1,2,3,4,5))  # 15 출력
print(mul(1,2,3,4,5))  # 120 출력
