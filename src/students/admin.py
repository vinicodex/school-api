from django.contrib import admin
from src.students.models import Student
from src.enrollments.admin import EnrollmentInline, AttendanceInline

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    list_per_page = 20
    inlines = [EnrollmentInline, AttendanceInline]
