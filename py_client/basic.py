import requests
import json
endpoint='http://127.0.0.1:8000/project/'
data = {'title': 'Rony', 'name': 'Rony_Ahemd', 'rmail': 'ro@gmail.com'}


get_value=requests.get(endpoint)
# get_value=requests.get(endpoint)
print(get_value.json())