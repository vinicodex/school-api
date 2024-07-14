from django.core.management.base import BaseCommand
from faker import Faker
import random
from core.models import Student, Teacher, Class, Grade, Attendance

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        Student.objects.all().delete()
        Teacher.objects.all().delete()
        Class.objects.all().delete()
        Grade.objects.all().delete()
        Attendance.objects.all().delete()

        teachers = []
        for _ in range(100):
            teacher = Teacher.objects.create(name=fake.name())
            teachers.append(teacher)
        self.stdout.write(self.style.SUCCESS('Successfully created 100 teachers'))

        students = []
        for _ in range(1000):
            student = Student.objects.create(name=fake.name(), birth_date=fake.date_of_birth())
            students.append(student)
        self.stdout.write(self.style.SUCCESS('Successfully created 1000 students'))

        classes = []
        for _ in range(100):
            teacher = random.choice(teachers)
            class_ = Class.objects.create(name=fake.word(), teacher=teacher)
            class_.students.set(random.sample(students, 30)) 
            classes.append(class_)
        self.stdout.write(self.style.SUCCESS('Successfully created 100 classes'))

        for student in students:
            for class_ in random.sample(classes, 5):
                Grade.objects.create(student=student, class_assigned=class_, grade=random.uniform(0, 10))
        self.stdout.write(self.style.SUCCESS('Successfully created grades for students'))

        for student in students:
            for class_ in random.sample(classes, 5):
                for _ in range(20):
                    Attendance.objects.create(student=student, class_assigned=class_, date=fake.date_this_year(), present=random.choice([True, False]))
        self.stdout.write(self.style.SUCCESS('Successfully created attendance records for students'))
