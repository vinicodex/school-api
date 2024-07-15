from django.urls import include, path
from rest_framework.routers import DefaultRouter
from src.classes.views import ClassViewSet

app_name = 'classes'

router = DefaultRouter()
router.register(r'classes', ClassViewSet, basename='classes')

urlpatterns = [
    path('', include(router.urls)),
]
