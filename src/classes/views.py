from rest_framework import viewsets
from src.classes.models import Class


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
