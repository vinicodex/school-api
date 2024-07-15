from django.contrib import admin
from src.classes.models import Class


class ClassInline(admin.TabularInline):
    model = Class
    extra = 0

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    model = Class
    list_display = ("class_name", "teacher")
