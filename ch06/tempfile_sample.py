import random
import tempfile


def sumfile(f):
    result = 0
    for line in f.readlines():
        num = int(line)
        result += num
    return result


tf = tempfile.TemporaryFile(mode='w+')
for i in range(10):
    num = random.randint(1, 100)
    tf.write(str(num))
    tf.write("\n")

tf.seek(0)  # 파일 오프셋을 처음으로 이동시킨다.
result = sumfile(tf)
tf.close()

print(result)
