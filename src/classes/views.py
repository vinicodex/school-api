from rest_framework import viewsets
from src.classes.models import Class
from src.classes.serializers import ClassSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
