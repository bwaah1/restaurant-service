from django.test import TestCase

from restaurant.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_parameters_is_valid(self) -> None:
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test_first",
            "last_name": "Test_last",
            "years_of_experience": 45
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
