# consumer.py
import pika
from django.conf import settings

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def consume_messages():
    credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=credentials
        )
    )
    channel = connection.channel()

    channel.queue_declare(queue='create_student')

    channel.basic_consume(queue='create_student', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
