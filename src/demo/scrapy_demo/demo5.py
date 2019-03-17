import django

import requests

headers = {"a":"1"}
resonse = requests.get("http://www.baidu.com", headers=headers)
print(resonse.text)
print(resonse.headers)
print(resonse.status_code)

