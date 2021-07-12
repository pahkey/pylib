import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts'
res = requests.get(url)
pprint.pprint(res.json())
