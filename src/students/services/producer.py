import pika
import json
from django.conf import settings

def send_message(student_data: dict) -> None:
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

    message = json.dumps(student_data)
    channel.basic_publish(exchange='', routing_key='create_student', body=message)
    print(f" [x] Sent {message}")
    connection.close()
