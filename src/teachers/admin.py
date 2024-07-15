from django.contrib import admin
from src.teachers.models import Teacher
from src.classes.admin import ClassInline


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    inlines = [ClassInline]