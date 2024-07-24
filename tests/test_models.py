from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Cook, Dish, DishType


class ModelsTest(TestCase):
    def test_dish_type_str(self) -> None:
        obj = DishType.objects.create(
            name="test_name",
        )
        self.assertEqual(str(obj), obj.name)

    def test_cook_str(self) -> None:
        obj = Cook.objects.create(
            username="test_username",
            first_name="test_first_name",
            last_name="test_last_name"
        )
        self.assertEqual(
            str(obj),
            f"{obj.username} ({obj.first_name} {obj.last_name})"
        )

    def test_dish_str(self) -> None:
        obj_manufacturer = DishType.objects.create(
            name="test_name",
        )
        obj = Dish.objects.create(
            name="test_name",
            description="test_description",
            price=55.55,
            dish_type=obj_manufacturer,
        )
        self.assertEqual(str(obj), obj.name)

    def test_create_cook_with_password(self) -> None:
        username = "123"
        password = "password123"
        years_of_experience = 45

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
