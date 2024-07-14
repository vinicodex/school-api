# core/serializers.py
from rest_framework import serializers
from .models import Student, Teacher, Class, Grade, Attendance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name',]

class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Class
        fields = ['class_name', 'teacher']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendedClassSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    teacher = TeacherSerializer()
    dates_attended = serializers.ListField(child=serializers.DateField())

class AttendedClassesResponseSerializer(serializers.Serializer):
    total_classes_attended = serializers.IntegerField()
    classes = AttendedClassSerializer(many=True)