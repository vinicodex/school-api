from django.core.exceptions import ValidationError
from django.db import models

from src.classes.models import Class
from src.students.models import Student


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()

    def __str__(self):
        return f"{self.student.name} - {self.class_assigned.class_name} on {self.date}"

    def clean(self):
        if not Enrollment.objects.filter(student=self.student, class_assigned=self.class_assigned).exists():
            raise ValidationError(f'Student {self.student.name} is not enrolled in class {self.class_assigned.class_name}.')
