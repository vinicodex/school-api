from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)

        student_detail = {
            'id': student.id,
            'name': student.name,
            'birth_date': student.birth_date,
            'is_active': student.is_active,
            'created_at': student.created_at,
            'updated_at': student.updated_at,
            'classes': []
        }

        enrollments = student.enrollment_set.all()

        for enroll in enrollments:
            class_detail = {
                'id': enroll.class_assigned.id,
                'class_name': enroll.class_assigned.class_name,
                'teacher': {
                    'id': enroll.class_assigned.teacher.id,
                    'name': enroll.class_assigned.teacher.name,
                },
            }
            student_detail['classes'].append(class_detail)

        return Response(student_detail)

    def destroy(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        student.is_active = False
        student.save()
        return Response({'status': 'student set to inactive'})

    @action(detail=True, methods=['get'], url_path='detailed')
    def get_student_v2(self, request, pk=None):
        student = get_object_or_404(
            Student.objects.prefetch_related(
                'enrollment_set__class_assigned__teacher'
            ),
            pk=pk
        )

        serializer = StudentSerializer(student)
        return Response(serializer.data)

