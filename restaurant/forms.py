from django import forms
from django.contrib.auth.forms import UserCreationForm

from restaurant.models import Cook, DishType, Dish


class CookModelSearchForm(forms.ModelForm):
    username = forms.CharField(max_length=255, required=False, label="")

    class Meta:
        model = Cook
        fields = ['username']


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class DishTypeModelSearchForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=False, label="")

    class Meta:
        model = DishType
        fields = ['name']


class DishModelSearchForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=False, label="")

    class Meta:
        model = Dish
        fields = ['name']