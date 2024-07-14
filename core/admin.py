from django.contrib import admin
from .models import Student, Teacher, Class, Grade, Attendance

class ClassInline(admin.TabularInline):
    model = Class.students.through
    extra = 1
    verbose_name = 'Class'
    verbose_name_plural = 'Classes'

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    inlines = [ClassInline, GradeInline]
    list_per_page = 20


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'teacher')
    search_fields = ('class_name',)
    list_filter = ('teacher',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_assigned', 'grade')
    search_fields = ('student__name', 'class_assigned__name')
    list_filter = ('class_assigned',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_assigned', 'date', 'present')
    search_fields = ('student__name', 'class_assigned__name')
    list_filter = ('class_assigned', 'date', 'present')
    list_select_related = True