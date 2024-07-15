from rest_framework import serializers
from src.enrollments.models import Enrollment, Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['student', 'class_assigned', 'date', 'present']

    def validate(self, data):
        student = data.get('student')
        class_assigned = data.get('class_assigned')

        if not Enrollment.objects.filter(student=student, class_assigned=class_assigned).exists():
            raise serializers.ValidationError(f'O estudante {student.name} não está matriculado na classe {class_assigned.class_name}.')

        return data
