from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from restaurant.forms import (
    CookModelSearchForm,
    CookCreationForm,
    DishTypeModelSearchForm,
    DishModelSearchForm,
    DishCreationForm
)
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


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    queryset = Cook.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs) -> QuerySet:
        context = super(CookListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = CookModelSearchForm(initial={"username": username})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Cook.objects.all()

        username = self.request.GET.get("username")

        if username:
            return queryset.filter(username__icontains=username)

        return queryset


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    success_url = reverse_lazy("restaurant:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("restaurant:cook-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    queryset = DishType.objects.all()
    context_object_name = "dish_type_list"

    def get_context_data(self, *, object_list=None, **kwargs) -> QuerySet:
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeModelSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = DishType.objects.all()

        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ["name"]
    template_name = "restaurant/dish_type_form.html"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ["name"]
    success_url = reverse_lazy("restaurant:dish-type-list")
    template_name = "restaurant/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dish-type-list")
    template_name = "restaurant/dish_type_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs) -> QuerySet:
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishModelSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Dish.objects.select_related("dish_type")

        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


@login_required
def toggle_assign_to_dish(request, pk) -> HttpResponse:
    cook = Cook.objects.get(id=request.user.id)
    if (
            Dish.objects.get(id=pk) in cook.dishes.all()
    ):
        cook.dishes.remove(pk)
    else:
        cook.dishes.add(pk)
    return HttpResponseRedirect(reverse_lazy("restaurant:dish-detail", args=[pk]))


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishCreationForm


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishCreationForm

    def get_success_url(self) -> str:
        return reverse("restaurant:dish-detail", kwargs={"pk": self.object.pk})


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")
