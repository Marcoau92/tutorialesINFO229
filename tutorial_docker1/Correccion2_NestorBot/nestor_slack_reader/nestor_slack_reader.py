#!/usr/bin/env python
import pika
import sys
import time
import os

time.sleep(120)

HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#Creamos el exchange 'nestor' de tipo 'fanout'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

message1 = "[traducir] Quiero ver una pelicula!"

message2 = "[wikipedia] Joe Biden"

#Publicamos los mensajes a través del exchange 'nestor' 
channel.basic_publish(exchange='nestor', routing_key="traducir", body=message1)

channel.basic_publish(exchange='nestor', routing_key="wikipedia", body=message2)

print(" [x] Sent %r" % message1)
print(" [x] Sent %r" % message2)
connection.close()
