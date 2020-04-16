#!/usr/bin/env python
import pika

parameters = pika.URLParameters('amqp://demo_user:demo_password@demo_rabbitmq_ip:5672/%2F')
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
