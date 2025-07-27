from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .helpers import create_admin_user_and_login, create_user_and_login, create_sweet

class PurchaseTests(APITestCase):
    def setUp(self):
        self.token = create_user_and_login(self.client)
        self.sweet = create_sweet()

    def test_purchase_sweet_success(self):
        """
         Red: Wrong expected status — expecting failure
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('purchase-sweet', args=[self.sweet.id])
        response = self.client.post(url, {"quantity": 2})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # ❌ wrong on purpose
        self.assertNotIn("Successfully purchased", response.data.get('message', ''))  # ❌ wrong on purpose

    def test_purchase_sweet_fail_exceed_quantity(self):
        """
         Red: Expecting wrong status — will fail
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('purchase-sweet', args=[self.sweet.id])
        response = self.client.post(url, {"quantity": 9999})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ❌ wrong on purpose

    def test_purchase_sweet_invalid_id(self):
        """
         Red: Expecting wrong status — will fail
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('purchase-sweet', args=[9999])
        response = self.client.post(url, {"quantity": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ❌ wrong on purpose
