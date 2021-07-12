import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')

args = parser.parse_args()

if args.add:
    print("합은 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("곱은 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))
