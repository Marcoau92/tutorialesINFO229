import os
import pika
import time
from youtubesearchpython import VideosSearch

time.sleep(30)


########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="youtube", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="youtube")

########## ESPERA Y HACE UN BUSQUEDA WIKIPEDIA CUANDO RECIBE UN MENSAJE ####

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(body)
    result = []
    if str(body).startswith("b'[youtube]"):
        query = str(body)[11:-1]
        print(query)
        videosSearch = VideosSearch(query, limit = 1).result()['result']
        for video_data in videosSearch:
            print(video_data['link'])
            result.append(video_data['link'])

        print(result)

        ########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
        for link in result:
            channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body=query+":"+link)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################

