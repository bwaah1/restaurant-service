from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

COOK_LIST_URL = reverse("restaurant:cook-list")


class PublicCookListTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self) -> None:
        res = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDriverListTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_driver_list(self) -> None:
        get_user_model().objects.create_user(
            username="123",
            password="password123",
            years_of_experience=45
        )
        get_user_model().objects.create_user(
            username="345",
            password="password345",
            years_of_experience=45
        )
        res = self.client.get(COOK_LIST_URL)
        self.assertEqual(res.status_code, 200)
