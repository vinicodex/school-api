from django.core.management.base import BaseCommand
from django.utils import timezone
from src.students.models import Student
from src.teachers.models import Teacher
from src.classes.models import Class
from src.enrollments.models import Enrollment, Attendance
from faker import Faker

class Command(BaseCommand):
    help = 'Creates 20 students, 2 teachers, classes, enrollments, and attendances'

    def handle(self, *args, **kwargs):
        fake = Faker()

        teachers = []
        for _ in range(2):
            teacher = Teacher.objects.create(
                name=fake.name(),
                is_active=True,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            teachers.append(teacher)

        classes = []
        for i in range(3):
            class_obj = Class.objects.create(
                class_name=fake.word(),
                teacher=teachers[i % 2],
                is_active=True,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            classes.append(class_obj)

        students = []
        for _ in range(20):
            student = Student.objects.create(
                name=fake.name(),
                birth_date=fake.date_of_birth(minimum_age=5, maximum_age=18),
                is_active=True,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            students.append(student)

        for student in students:
            class_obj = fake.random_element(classes)
            enrollment = Enrollment.objects.create(
                student=student,
                class_assigned=class_obj,
                enrolled_at=timezone.now()
            )

            for _ in range(5):
                Attendance.objects.create(
                    student=student,
                    class_assigned=class_obj,
                    date=fake.date_this_year(),
                    present=fake.boolean(chance_of_getting_true=75)
                )

        self.stdout.write(self.style.SUCCESS('Successfully created 20 students, 2 teachers, classes, enrollments, and attendances'))
