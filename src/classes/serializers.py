from rest_framework import serializers
from src.classes.models import Class
from src.students.models import Student
from src.teachers.models import Teacher


class ClassSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False)
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True, required=False)

    class Meta:
        model = Class
        fields = ['id', 'class_name', 'teacher', 'students', 'is_active', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Update class name
        instance.class_name = validated_data.get('class_name', instance.class_name)

        teacher_data = validated_data.get('teacher', None)
        if teacher_data:
            instance.teacher = teacher_data

        students_data = validated_data.get('students', None)
        if students_data:
            instance.students.set(students_data)

        instance.save()
        return instance
