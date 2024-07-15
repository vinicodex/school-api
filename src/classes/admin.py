from django.contrib import admin
from src.classes.models import Class


class ClassInline(admin.TabularInline):
    model = Class
    extra = 1
    show_change_link = True


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    model = Class
    list_display = ("class_name", "teacher")
