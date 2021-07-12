import linecache
import random

no = random.randint(1, 100)
print(linecache.getline('saying.txt', no))
