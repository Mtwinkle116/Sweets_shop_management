from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .helpers import create_admin_user_and_login, create_user_and_login, create_sweet

class PurchaseTests(APITestCase):
    def setUp(self):
        self.token = create_user_and_login(self.client)
        self.sweet = create_sweet()

    def test_purchase_sweet_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('purchase-sweet', args=[self.sweet.id])
        response = self.client.post(url, {"quantity": 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Successfully purchased", response.data['message'])

    def test_purchase_sweet_fail_exceed_quantity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('purchase-sweet', args=[self.sweet.id])
        response = self.client.post(url, {"quantity": 9999})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_purchase_sweet_invalid_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('purchase-sweet', args=[9999])
        response = self.client.post(url, {"quantity": 1})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
