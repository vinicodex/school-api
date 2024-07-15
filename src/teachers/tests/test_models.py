
import pytest
from django.utils import timezone
from src.teachers.models import Teacher

@pytest.mark.django_db
def test_teacher_creation():
    teacher = Teacher.objects.create(name='John Doe')
    assert teacher.name == 'John Doe'
    assert teacher.is_active is True
    assert teacher.created_at <= timezone.now()
    assert teacher.updated_at <= timezone.now()

@pytest.mark.django_db
def test_teacher_default_values():
    teacher = Teacher.objects.create(name='Jane Smith')
    assert teacher.is_active is True

def test_teacher_str():
    teacher = Teacher(name='Jane Doe')
    assert str(teacher) == 'Jane Doe'
