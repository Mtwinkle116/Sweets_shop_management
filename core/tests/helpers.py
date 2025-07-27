from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from core.models import Sweet

def create_user_and_login(client):
    user = get_user_model().objects.create_user(username="cust", password="test123")
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

def create_admin_user_and_login(client):
    user = get_user_model().objects.create_user(username="admin", password="admin123", is_admin=True)
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

def create_sweet():
    return Sweet.objects.create(name="Barfi", price=10, quantity=20)
