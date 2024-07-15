import csv
from django.core.management.base import BaseCommand
from src.students.services.producer import send_message

class Command(BaseCommand):
    help = 'Import students from a CSV file and send to RabbitMQ'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student_data = {
                    'name': row['name'],
                    'birth_date': row['birth_date'],
                    'is_active': row['is_active'].lower() == 'true'
                }
                send_message(student_data)
        self.stdout.write(self.style.SUCCESS(f"Sent message for student: {student_data['name']}"))


