from django.contrib import admin
from src.students.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    # inlines = [ClassInline, GradeInline]
    list_per_page = 20