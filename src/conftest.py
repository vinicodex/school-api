import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    user.is_staff = True  # Give the user staff status if needed for admin permissions
    user.save()
    return user

@pytest.fixture
def bearer_token(create_user):
    refresh = RefreshToken.for_user(create_user)
    return str(refresh.access_token)

@pytest.fixture
def authenticated_api_client(api_client, bearer_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + bearer_token)
    return api_client
