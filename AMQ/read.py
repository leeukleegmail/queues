import time
import json

import pika

from settings import queue_name, mq_host, json_value


def perform_action(msg):
    print(" [x] Message Received " + str(json.loads(msg)[json_value]))
    ### do task
    return;


connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host))
channel = connection.channel()
channel.queue_declare(queue=queue_name)


def callback(ch, method, properties, body):
    perform_action(body)


channel.basic_consume(queue_name,
                      callback,
                      auto_ack=True)
channel.start_consuming()
connection.close()
