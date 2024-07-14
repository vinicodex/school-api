from django.contrib import admin
from school_api import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="School API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="marcos@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('students/', include('src.students.urls', namespace='students_v1')),
        path('teachers/', include('src.teachers.urls', namespace='teachers_v1')),
        path('classes/', include('src.classes.urls', namespace='classes_v1')),
    ])),    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
