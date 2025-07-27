from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .helpers import create_admin_user_and_login, create_sweet

class SweetCRUDTests(APITestCase):
    def setUp(self):
        self.admin_token = create_admin_user_and_login(self.client)

    def test_create_sweet_success(self):
        url = reverse('sweet-list-create')
        data = {
            "name": "Ladoo",
            "price": 20,
            "quantity": 100,
            "category": "Traditional"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_sweet_fail_if_not_admin(self):
        self.client.credentials()  # unauthenticated
        url = reverse('sweet-list-create')
        data = {"name": "Jalebi", "price": 25, "quantity": 50}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_sweet_success(self):
        sweet = create_sweet()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        url = reverse('sweet-update', args=[sweet.id])
        response = self.client.patch(url, {"price": 30})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_sweet(self):
        sweet = create_sweet()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        url = reverse('sweet-delete', args=[sweet.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
