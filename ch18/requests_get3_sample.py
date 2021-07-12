import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}
res = requests.get(url, params=params)
pprint.pprint(res.json())
