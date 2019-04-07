from requests.exceptions import RequestException
import requests
import re
import json
from multiprocessing import Pool

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page():
    pass

def write_to_file(content):
    with open("./result.txt", 'a', encoding='utf-8') as file:
        file.write(json.dumps(content, ensure_ascii=False))

def main():
    url  = "https://maoyan.com/board/4?"
    html = get_one_page(url)
    print(html)

if __name__ == "__main__":
    pool = Pool()
    pool.map(main(), [1, 2 ,3])