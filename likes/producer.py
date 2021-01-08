import pika
import json

params = pika.URLParameters(
    'amqps://rnyipnra:gtXyo9mR1WI9zTn9bKEpRjO5yTNuUtKo@lionfish.rmq.cloudamqp.com/rnyipnra')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='product',
                          body=json.dumps(body), properties=properties)

def publish2(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='user',
                          body=json.dumps(body), properties=properties)
