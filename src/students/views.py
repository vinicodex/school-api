from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

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
