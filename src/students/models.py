from django.db import models
from django.utils import timezone

class StudentQuerySet(models.QuerySet):
    def active_students_in_2024(self):
        start_date = timezone.datetime(2024, 1, 1)
        end_date = timezone.datetime(2024, 12, 31, 23, 59, 59)
        return self.filter(is_active=True, created_at__range=(start_date, end_date))

class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)

    def active_students_in_2024(self):
        return self.get_queryset().active_students_in_2024()

class Student(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = StudentManager()

    def __str__(self):
        return self.name
