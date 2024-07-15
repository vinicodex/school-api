import csv
from django.core.management.base import BaseCommand
from src.students.models import Student
class Command(BaseCommand):
    help = 'Import students from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        students_to_create = []

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = Student(
                    name=row['name'],
                    birth_date=row['birth_date'],
                    is_active=row['is_active'].lower() == 'true'
                )
                students_to_create.append(student)

                if len(students_to_create) >= 1000:
                    Student.objects.bulk_create(students_to_create)
                    students_to_create = []

            if students_to_create:
                Student.objects.bulk_create(students_to_create)

        self.stdout.write(self.style.SUCCESS('Successfully imported students'))
