from django.urls import path

from . import views

app_name = "bnb"
urlpatterns = [
    path("", views.index, name="index"),
]

