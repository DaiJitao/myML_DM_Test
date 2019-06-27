import time
from kafka import KafkaProducer
from kafka import KafkaConsumer

topic = "demo"
host = "10.129.1.16:9092"


def produce(times):
    producer = KafkaProducer(bootstrap_servers=host)
    for _ in range(times):
        time.sleep(1)
        producer.send(topic=topic, key="name", value="daijitao")
        producer.send(topic=topic, key="12", value="lixiang")
    producer.flush()
    print("写入完毕！")


def consume():
    consumer = KafkaConsumer(bootstrap_servers=host)
    consumer.subscribe(topic)
    for _ in consumer:
        produce(_)


produce(20)
