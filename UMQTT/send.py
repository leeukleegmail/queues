from umqtt.simple import MQTTClient
from settings import queue_topic, mq_host, send_client

c = MQTTClient(send_client, mq_host)
c.connect()
message = bytes(str("hello"), 'utf-8')
c.publish(str.encode(queue_topic), message)
c.disconnect()
