import redis
import time
import threading

conn = redis.Redis()
print(conn.get('key1'))
print(conn.incr('key1'))

def trans():
    pipline = conn.pipeline()
    pipline.incr('trans')
    time.sleep(.1)
    pipline.incr('trans', -1)
    print(pipline.execute()[0])

for i in range(3):
    threading.Thread(target=trans).start()
time.sleep(.5)