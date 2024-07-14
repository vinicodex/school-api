from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.api.v2.viewsets import StudentViewSetV2, AttendanceViewSetV2
from school_api import settings

router = DefaultRouter()

router.register(r'students', StudentViewSetV2)
router.register(r'attendance', AttendanceViewSetV2)


urlpatterns = [
    path('', include(router.urls)),
]