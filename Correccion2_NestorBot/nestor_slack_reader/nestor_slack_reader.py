import os
import logging
import time
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import pika

#time.sleep(45)

############ CONEXION RABBITMQ ##############

HOST = os.environ['RABBITMQ_HOST']
connection = None
channel = None
while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=HOST))
        channel = connection.channel()
        channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)
        break
    except:
        connection = None
        channel = None
        print("error al conectar a Rabbit...reintentando")
print("conectado a rabbit")
#Creamos el exchange 'nestor' de tipo 'fanout'



app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event injestion.
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))
# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):

    # Get the event data from the payload
    event = payload.get("event", {})
    message = payload["event"]

    # Get the text from the event that came through
    text = event.get("text")
    print(message.get("text"))
    print("hola")
    if text.startswith("[traducir]"):
        channel.basic_publish(exchange='nestor', routing_key="traducir", body=text)

    if text.startswith("[wikipedia]"):
        channel.basic_publish(exchange='nestor', routing_key="wikipedia", body=text)

    if text.startswith("[youtube]"):
        channel.basic_publish(exchange='nestor', routing_key="youtube", body=text)

if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=3000)