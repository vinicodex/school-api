import pytest
from src.teachers.models import Teacher
from src.teachers.serializers import TeacherSerializer

@pytest.mark.django_db
def test_teacher_serializer_serialization():
    teacher = Teacher.objects.create(name='Jane Smith', is_active=True)

    serializer = TeacherSerializer(teacher)
    data = serializer.data

    assert data['name'] == 'Jane Smith'

@pytest.mark.django_db
def test_teacher_serializer_deserialization():
    data = {
        'name': 'John Doe',
        'is_active': False
    }

    serializer = TeacherSerializer(data=data)
    assert serializer.is_valid()
    teacher = serializer.save()

    assert teacher.name == 'John Doe'
    assert teacher.is_active == True

@pytest.mark.django_db
def test_teacher_serializer_validation():
    data = {
        'is_active': True
    }

    serializer = TeacherSerializer(data=data)
    assert not serializer.is_valid()
    assert 'name' in serializer.errors

    data = {
        'name': 'Jane Doe',
        'is_active': True
    }

    serializer = TeacherSerializer(data=data)
    assert serializer.is_valid()

