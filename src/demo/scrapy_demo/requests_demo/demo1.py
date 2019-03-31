import requests

url = "http://httpbin.org/post"

files = {'file': open('./data/test.txt', 'rb')}

response = requests.post(url=url, files=files)
print(response.url)
print(response.text)
print(response.content)
print(response.status_code)