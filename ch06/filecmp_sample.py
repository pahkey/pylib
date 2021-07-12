import filecmp

fd = filecmp.dircmp('a', 'b')

for a in fd.left_only:
    print("a: %s" % a)

for b in fd.right_only:
    print("b: %s" % b)

for x in fd.diff_files:
    print("x: %s" % x)
