import requests
import pprint
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Content-type': 'application/json; charset=utf-8'}
data = {
    'id': 1,
    'title': '제목을 수정',
    'body': '내용을 수정',
    'userId': 1,
}
res = requests.put(url, headers=headers, data=json.dumps(data))
pprint.pprint(res.json())
