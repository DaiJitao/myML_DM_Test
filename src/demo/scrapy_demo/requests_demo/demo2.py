import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError

base_url = ""

headers = {
    'Cookie': "",
    "Host": "",

}
proxy = None


def get_proxy():
    pool_url = "http://localhost:5000/get"
    res = requests.get(pool_url)
    try:
        if res.status_code == 200:
            return res.text
        return None
    except ConnectionError:
        return None


def get_html(url, count=5):
    global proxy
    try:
        if proxy:
            proxies = {'http': "http://" + proxy}
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 302:
            print("302")
            proxy = get_proxy()
            if proxy:
                # ip = get_proxy
                print("using proxy")
                return get_html(url)
            else:
                return None
    except ConnectionError as e:
        print("Error args", e.args)
        return get_html(url)


def get_index(keyword, page):
    data = {
        "query": keyword,
        "type": 2,
        "page": page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    print(html)
    return html
