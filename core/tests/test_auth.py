from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class AuthTests(APITestCase):

    def test_register_user_success(self):
        url = reverse('register')
        data = {
            "username": "testuser",
            "password": "testpass123",
            "email": "test@example.com",
            "is_admin": False
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # ✅ Fixed: should be 201

    def test_register_user_missing_password(self):
        url = reverse('register')
        data = {
            "username": "nouser",
            "email": "no@example.com",
            "is_admin": False
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # ✅ Fixed: missing password returns 400

    def test_login_user_success(self):
        user = get_user_model().objects.create_user(username="loginuser", password="pass123")
        url = reverse('token_obtain_pair')
        data = {"username": "loginuser", "password": "pass123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ✅ Fixed: valid login
        self.assertIn("access", response.data)  # ✅ Fixed: token should be in response

    def test_login_user_invalid_credentials(self):
        url = reverse('token_obtain_pair')
        data = {"username": "wrong", "password": "wrongpass"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # ✅ Fixed: invalid credentials
