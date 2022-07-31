import pika

from settings import mq_host, queue_name, json_value

connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host))
channel = connection.channel()
channel.queue_declare(queue=queue_name)

for i in range(10000):
    message = '{{"{}" : "hello world {}"}}'.format(json_value, i)

    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message)
    print(" [x] Sent {}".format(message))

connection.close()
