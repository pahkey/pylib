import asyncio
import time


async def sleep():
    await asyncio.sleep(1)


async def sum(name, numbers):
    start = time.time()
    total = 0
    for number in numbers:
        await sleep()
        total += number
        print(f'작업중={name}, number={number}, total={total}')
    end = time.time()
    print(f'작업명={name}, 걸린시간={end-start}')
    return total


async def main():
    start = time.time()

    task1 = asyncio.create_task(sum("A", [1, 2]))
    task2 = asyncio.create_task(sum("B", [1, 2, 3]))

    await task1
    await task2

    result1 = task1.result()
    result2 = task2.result()

    end = time.time()
    print(f'총합={result1+result2}, 총시간={end-start}')


if __name__ == "__main__":
    asyncio.run(main())
