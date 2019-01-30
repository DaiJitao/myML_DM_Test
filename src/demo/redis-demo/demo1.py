
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

run_publisher()