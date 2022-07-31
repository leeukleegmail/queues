import paho.mqtt.client as mqtt
import time

from settings import mq_host, read_client, queue_topic


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))


client = mqtt.Client(read_client)
client.connect(mq_host)
client.loop_start()
client.subscribe(queue_topic)

while True:
    client.on_message = on_message
#
# time.sleep(30)
# client.loop_stop()
