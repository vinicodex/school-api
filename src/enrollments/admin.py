from django.contrib import admin
from src.enrollments.models import Enrollment, Attendance


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1
    show_change_link = True
    fk_name = 'student'


class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 1
    show_change_link = True
    fk_name = 'student'

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    model = Enrollment
    list_display = ('student', 'enrolled_at')
