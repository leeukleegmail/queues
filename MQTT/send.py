import random

import paho.mqtt.client as mqtt
import time

from settings import queue_topic, mq_host, send_client

client = mqtt.Client(send_client)
client.connect(host=mq_host)

# while True:
colour = random.choice(["blue", "green", "red"])
message = '{{"colour" : "{}", "value" : 1}}'.format(colour)
client.publish(queue_topic, message, retain=True)
print("Just published {} to topic {}".format(message, queue_topic))
client.disconnect()
# time.sleep(3)
