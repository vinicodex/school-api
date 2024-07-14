from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Prefetch
from rest_framework.decorators import action
from .models import Student, Teacher, Class, Grade, Attendance
from .serializers import StudentSerializer, TeacherSerializer, ClassSerializer, GradeSerializer, AttendanceSerializer, AttendedClassesResponseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def attended_classes(self, request, pk=None):
        student = self.get_object()
        
        attendance_records = Attendance.objects.filter(
            student=student,
            date__year=2024,
            present=True
        )
        
        classes_attended = set(record.class_assigned for record in attendance_records)
        
        classes_data = []
        for class_attended in classes_attended:
            class_data = {
                'class_id': int(class_attended.id),
                'teacher': {
                    'name': class_attended.teacher.name
                },
                'dates_attended': [record.date for record in attendance_records if record.class_assigned == class_attended]
            }
            classes_data.append(class_data)
        
        response_data = {
            'total_classes_attended': attendance_records.count(),
            'classes': classes_data
        }
        
        response_serializer = AttendedClassesResponseSerializer(response_data)
        
        return Response(response_serializer.data)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
