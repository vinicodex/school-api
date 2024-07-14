from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from src.enrollments.models import Attendance
from src.students.models import Student
from src.students.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(is_active=True)
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        student = self.get_object()

        if not student.is_active:
            return Response(
                {"detail": "Cannot delete an inactive student."},
                status=HTTP_400_BAD_REQUEST
            )

        student.is_active = False
        student.save()

        return Response(
            {"detail": "Student has been set to inactive."},
            status=HTTP_200_OK
        )

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
                'dates_attended': [record.date for record in attendance_records if
                                   record.class_assigned == class_attended]
            }
            classes_data.append(class_data)

        response_data = {
            'total_classes_attended': attendance_records.count(),
            'classes': classes_data
        }

        response_serializer = AttendedClassesResponseSerializer(response_data)

        return Response(response_serializer.data)
