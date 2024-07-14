from rest_framework import serializers
from src.classes.models import Class
from src.teachers.serializers import TeacherSerializer


class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Class
        fields = ['class_name', 'teacher']