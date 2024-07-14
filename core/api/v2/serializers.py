# src/core/serializers.py
from rest_framework import serializers
from core.models import Student, Teacher, Class, Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'birth_date']

class ClassSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    students = StudentSerializer(many=True, read_only=True)
    attendances = AttendanceSerializer(many=True, read_only=True, source='attendance_set')

    class Meta:
        model = Class
        fields = ['id', 'class_name', 'teacher', 'students', 'attendances']
