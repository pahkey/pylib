import requests
import pprint
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Content-type': 'application/json; charset=utf-8'}
data = {
    'title': 'Hello',
}
res = requests.patch(url, headers=headers, data=json.dumps(data))
pprint.pprint(res.json())
