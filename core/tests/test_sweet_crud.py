from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .helpers import create_admin_user_and_login

class SweetCRUDTests(APITestCase):
    def setUp(self):
        self.admin_token = create_admin_user_and_login(self.client)

    def test_create_sweet_success(self):
        """
        Red: This test is intentionally incorrect — expects 400 instead of 201
        """
        url = reverse('sweet-list-create')
        data = {
            "name": "Ladoo",
            "price": 20,
            "quantity": 100,
            "category": "Traditional"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # ❌ wrong on purpose

    def test_create_sweet_fail_if_not_admin(self):
        """
        Red: This test is also incorrect — expects 201 instead of 401/403
        """
        self.client.credentials()  # unauthenticated
        url = reverse('sweet-list-create')
        data = {
            "name": "Jalebi",
            "price": 25,
            "quantity": 50,
            "category": "Fried"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # ❌ wrong on purpose
