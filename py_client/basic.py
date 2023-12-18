import requests
import json
endpoint='http://127.0.0.1:8000/snippets/'
data = {'title': 'Rony', 'name': 'Rony_Ahemd', 'rmail': 'ro@gmail.com'}


get_value=requests.post(endpoint,json=data)
# get_value=requests.get(endpoint)
print(get_value.json())