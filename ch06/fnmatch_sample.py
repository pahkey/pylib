import fnmatch
import os

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, 'a???[0-9].py'):
        print(filename)
