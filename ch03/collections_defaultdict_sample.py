from collections import defaultdict

text = "Life is too short, You need python."

d = defaultdict(int)
for c in text:
    d[c] += 1

print(dict(d))
