from rest_framework import serializers

from src.classes.models import Class
from src.students.models import Student
from src.teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']

class ClassAssignedSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Class
        fields = ['id', 'class_name', 'teacher']

class StudentSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'birth_date', 'is_active', 'created_at', 'updated_at', 'classes']

    def get_classes(self, student):
        enrollments = student.enrollment_set.all()
        return ClassAssignedSerializer([enroll.class_assigned for enroll in enrollments], many=True).data
