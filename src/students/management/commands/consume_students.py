import pika
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from src.students.models import Student

class Command(BaseCommand):
    help = 'Consume the RabbitMQ queue and create students'

    def handle(self, *args, **kwargs):
        self.consume_messages()

    def consume_messages(self):
        credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                credentials=credentials
            )
        )
        channel = connection.channel()

        channel.queue_declare(queue='class_enrollment')

        def callback(ch, method, properties, body):
            message = body.decode('utf-8')
            data = json.loads(message)
            self.create_student(data)

        channel.basic_consume(queue='create_student', on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    def create_student(self, data):
        student, created = Student.objects.get_or_create(
            name=data['name'],
            birth_date=data['birth_date'],
            defaults={'is_active': data['is_active']}
        )
        if created:
            print(f"Created student: {student.name}")
        else:
            print(f"Student already exists: {student.name}")
