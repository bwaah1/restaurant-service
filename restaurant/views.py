from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from restaurant.models import DishType, Dish, Cook


@login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    num_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_types": num_types,
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_visits": num_visits + 1,
    }

    return render(request, "restaurant/index.html", context=context)
