import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts/1'
res = requests.delete(url)
pprint.pprint(res.json())
