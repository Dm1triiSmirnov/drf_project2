from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from wallet.models import Wallet


class WalletTests(APITestCase):
    def setUp(self):
        """Create 'testuser' and perform authentication"""

        client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@testuser.com", password="testuser"
        )
        response = client.post(
            "/auth/token/", {"username": "testuser", "password": "testuser"}
        )
        self.token = response.json()["access"]
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def test_create_wallet(self):
        """Test fto create wallet"""

        url = reverse("wallet_list_create")
        data = {"type": "Visa", "currency": "RUB"}
        response = self.client.post(url, data, format="json", headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(response.data["type"], "Visa")
        self.assertEqual(response.data["currency"], "RUB")
        self.assertEqual(response.data["balance"], "100.00")

    def test_retrieve_wallet(self):
        """Test to retrieve wallet details"""

        wallet = Wallet.objects.create(
            name="JO72KFZ1",
            type="Mastercard",
            currency="EUR",
            balance="0.00",
            user=self.user,
        )
        url = reverse("wallet_retrieve_destroy", kwargs={"name": wallet.name})
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(response.data[0]["name"], wallet.name)
        self.assertEqual(response.data[0]["type"], wallet.type)
        self.assertEqual(response.data[0]["currency"], wallet.currency)
        self.assertEqual(response.data[0]["balance"], wallet.balance)
        self.assertEqual(response.data[0]["user"], wallet.user_id)

    def test_delete_wallet(self):
        """Test to delete wallet"""

        wallet = Wallet.objects.create(
            name="JO72KFZ1",
            type="Mastercard",
            currency="EUR",
            balance="0.00",
            user=self.user,
        )
        url = reverse("wallet_retrieve_destroy", kwargs={"name": wallet.name})
        response = self.client.delete(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Wallet.objects.filter(pk=wallet.pk).exists())
        self.assertEqual(response.data["Message"], "Wallet has been deleted")

    def test_retrieve_wallets_list(self):
        """Test to retrieve all wallets for current user"""

        url = reverse("wallet_list_create")
        wallet1 = self.client.post(
            url,
            {"type": "Visa", "currency": "USD"},
            format="json",
            headers=self.headers,
        )
        wallet2 = self.client.post(
            url,
            {"type": "Mastercard", "currency": "RUB"},
            format="json",
            headers=self.headers,
        )
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Wallet.objects.count(), 2)
        self.assertEqual(response.data[0]["name"], wallet1.data["name"])
        self.assertEqual(response.data[0]["balance"], "3.00")
        self.assertEqual(response.data[1]["name"], wallet2.data["name"])
        self.assertEqual(response.data[1]["balance"], "100.00")
