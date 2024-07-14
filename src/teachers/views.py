from django.shortcuts import render
from rest_framework import viewsets
from src.teachers.models import Teacher
from src.teachers.serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
