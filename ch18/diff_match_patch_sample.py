from diff_match_patch import diff_match_patch

before = "Life is too short, you need python."
after = "Life is short, you need python language."

dmp = diff_match_patch()
diff = dmp.diff_main(before, after)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d)
