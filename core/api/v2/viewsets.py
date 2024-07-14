from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Prefetch
from rest_framework.decorators import action
from core.models import Student, Teacher, Class, Grade, Attendance
from core.pagination import CustomPagination
from core.api.v2.serializers import StudentSerializer, ClassSerializer, AttendanceSerializer


class AttendanceViewSetV2(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class StudentViewSetV2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(detail=True, methods=['get'])
    def attended_classes(self, request, pk=None):

        student = self.get_object()
        
        attendance_records = Attendance.objects.filter(
            student=student,
            date__year=2024,
            present=True
        ).select_related('class_assigned', 'class_assigned__teacher')

        classes_attended = set(record.class_assigned for record in attendance_records)
        response_data = {
            'total_classes_attended': attendance_records.count(),
            'classes': [
                {   
                    'class_id': class_attended.id,
                    'class_name': class_attended.class_name,
                    'teacher': class_attended.teacher.name,
                    'dates_attended': [
                        record.date for record in attendance_records if record.class_assigned == class_attended
                    ]
                }
                for class_attended in classes_attended
            ],
        }
        
        return Response(response_data)