import pytest
from rest_framework import status
from src.teachers.models import Teacher
@pytest.mark.django_db
def test_create_teacher(api_client, bearer_token):
    url = '/api/v1/teachers/'
    data = {
        'name': 'Jane Smith',
        'is_active': True
    }

    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + bearer_token)
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_retrieve_teacher(api_client, bearer_token):
    teacher = Teacher.objects.create(name='Jane Smith', is_active=True)
    url = f'/api/v1/teachers/{teacher.id}/'

    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + bearer_token)
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_teacher(api_client, bearer_token):
    teacher = Teacher.objects.create(name='Jane Smith', is_active=True)
    url = f'/api/v1/teachers/{teacher.id}/'
    data = {
        'name': 'Jane Doe',
        'is_active': False
    }

    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + bearer_token)
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_teacher(api_client, bearer_token):
    teacher = Teacher.objects.create(name='Jane Smith', is_active=True)
    url = f'/api/v1/teachers/{teacher.id}/'

    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + bearer_token)
    response = api_client.delete(url, format='json')
    assert response.status_code == status.HTTP_204_NO_CONTENT

