import http.client


def get_wikidocs(page):
    conn = http.client.HTTPSConnection("wikidocs.net")
    conn.request("GET", "/12")
    r = conn.getresponse()
    with open('wikidocs_%s.html' % page, 'wb') as f:
        f.write(r.read())
    conn.close()


if __name__ == "__main__":
    get_wikidocs(12)
