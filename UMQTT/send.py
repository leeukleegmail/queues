from umqtt.simple import MQTTClient
from settings import queue_topic, mq_host, send_client

c = MQTTClient(send_client, mq_host)
c.connect()
c.publish(str.encode(queue_topic), b"hello")
c.disconnect()
