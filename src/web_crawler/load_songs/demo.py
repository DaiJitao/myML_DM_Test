import requests

def demo1():
    url='http://play.baidu.com/data/music/songlink'
    data={'songIds':'100575177'}
    r=requests.post(url,data=data)
    if r.status_code == 200:
        print("访问成功")
        print(r.content.decode('UTF-8'))
        f=open('e:/data.txt','w',encoding='utf-8')
        f.write(r.content.decode('UTF-8'))
        f.close()
    else:
        print("error")

def demo2(url, saveDataPath):
    url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&songid=2498009'
    res = requests.get(url)
    if res.status_code == 200:
        print("ok 200")
        content = res.content.decode('utf-8')
        print(content)
        with open('e:/data.txt', 'w', encoding='utf-8') as file:
            file.write(content)
    else:
        print('error')

def demo3(url, save_path):
    """
    获取百度MV
    :return:
    """
    url = 'http://music.baidu.com/playmv/554869244'
    s = requests.session()
    headers = {'referer': 'http://music.baidu.com/mv',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
               }

    r = s.get(url, headers=headers)
    print(r)
    if r.status_code == 200:
        print("OK 200")
        a = r.content.decode('UTF-8')
        print(r)
        file_mp4 = a.split('data.push')[1].split('file_link":"')[1].replace('"});', '').replace(r"\\", r'').replace(
            '\/',
            '/').replace(
            "\n", '').strip()
        get_file = s.get(file_mp4)
        with open("E:/data.mp4", 'wb') as mp4:
            mp4.write(get_file.content)
    else:
        print("error")

if __name__ == "__main__":
    demo3(None, None)