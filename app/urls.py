from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("restaurant.urls", namespace="restaurant")),
    path("accounts/", include("django.contrib.auth.urls")),
]
