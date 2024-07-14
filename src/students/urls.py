from django.urls import include, path
from rest_framework.routers import DefaultRouter
from src.students.views import StudentViewSet
from school_api import settings

app_name = 'students'

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]