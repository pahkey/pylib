import requests
import pprint
import json

url = 'https://jsonplaceholder.typicode.com/posts'
headers = {'Content-type': 'application/json; charset=utf-8'}
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}

res = requests.post(url, headers=headers, data=json.dumps(data))
pprint.pprint(res.json())
