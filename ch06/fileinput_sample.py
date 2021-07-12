import fileinput
import glob

with fileinput.input(glob.glob("*.txt")) as f:
    for line in f:
        print(line)
