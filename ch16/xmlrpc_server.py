import urllib.request
from xmlrpc.server import SimpleXMLRPCServer


def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'


with SimpleXMLRPCServer(('localhost', 8000)) as server:
    server.register_introspection_functions()
    server.register_function(get_wikidocs, 'wikidocs')
    server.serve_forever()
