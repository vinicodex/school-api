from django.urls import include, path
from rest_framework.routers import DefaultRouter
from src.teachers.views import TeacherViewSet

app_name = 'teachers'

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]