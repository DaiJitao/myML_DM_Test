
import redis
import time
import threading

conn = redis.Redis()

def publisher(n):
    time.sleep(1)
    global conn
    for i in range(n):
        conn.publish('channel', i)
        time.sleep(1)

def run_publisher():
    threading.Thread(target=publisher, args=(3, )).start()
    pubsub = conn.pubsub()
    pubsub.subscribe(['channel'])
    cout = 0
    for item in pubsub.listen():
        print(item)
        cout += 1
        if cout == 4:
            pubsub.unsubscribe()
        if cout == 5:
            break

key = "key"
print(conn.get(key) == None)
print(conn.incr(key))
print(conn.incr(key, 15))
print(type(conn.set(key, 13)))
print(int(conn.get(key)))
print(conn.get(key))
print(conn.set(key, "daijitao"))
print(conn.substr(key, 1, 2))